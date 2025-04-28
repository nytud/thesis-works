import docker
import tarfile
import io
import re

class Emagyar:
    def __init__(self):
        self.tok = []
        self.morph = []
        self.lem = []
        self.pos = []
        self.dep = []
        self.head = []
        self._head_num = [] #this links the dep head by id
        self._ids = [] #every token has an id in the sentence it is in for dependency
        self.ner = []
        self.only_ner = []

    def run(self, fname, txt):
        #run emagyar through docker
        #for simulation, COMMENT FROM HERE
        succ = False
        try:
            client = docker.from_env()
            container = client.containers.run("mtaril/emtsv", detach=True)

        
            tar_stream = io.BytesIO()

            with open("currentinput.txt", "w") as f:
                f.write(txt)

            with tarfile.open(fileobj=tar_stream, mode="w") as tar:
                tar.add("currentinput.txt") #we must transfer the input as a file -> this makes a tarfile out of it

            tar_stream.seek(0)
            succ = container.put_archive(path="/app", data=tar_stream) #transfering the input file to docker
            
            if succ: #transfer was successful
                #run emagyar in the docker
                command = f"python3 ./main.py tok,spell,morph,pos,conv-morph,dep,chunk,ner -i ./currentinput.txt -o ana_emagyar_{fname}"
                result = container.exec_run(command)

                if result.exit_code == 0:
                    with open("eredmeny.tar", "wb") as f:
                        strm, status = container.get_archive(f"/app/ana_emagyar_{fname}") #get the result from docker
            
                        #transfer its contents to a local tar file
                        for chunk in strm:
                            f.write(chunk)
                    

                    #get the real contents from the tar file and put it to the designated directory
                    with tarfile.open("eredmeny.tar", "r") as tar:
                        tar.extractall("eredmenyek/emagyar", filter="data")

                else:
                    raise Exception(f"Sikertelen az elemzés lefuttatása {result.exit_code}")
            else:
                raise Exception("Sikertelen fájlátvitel, nem történt meg az elemzés")
        except Exception as e:
            raise Exception(f"e-magyar: Sikertelen elemzés, nem jött létre outputfile ({e})")           
        finally:
            #cleaning up the container
            container.stop()
            container.remove()

        if succ:
            self.__makelists(fname)
        """
        #for simulation, END COMMENT HERE
        #UNCOMMENT FROM HERE
        
        
        self.__makelists(fname)
        """
        #uncommentable simulation section ends here


    def print(self, fname):
        ret = []
        with open(f"eredmenyek/emagyar/ana_emagyar_{fname}", "r") as f:
            for line in f.readlines():
                ret.append(line.split("\t"))
        return ret
            

    def __makelists(self, fname):
        #emagyar gave us the results in its own format -> we have to process and transform it to work with it like we would with huspacy
        try:
            with open(f"eredmenyek/emagyar/ana_emagyar_{fname}") as f2:
                lines_raw = f2.read()
                lines = lines_raw.split('\n')

                #remove empty lines
                to_rem = []

                for i in range(0, len(lines)):
                    if len(lines[i]) == 0:
                        to_rem.append(i)

                for i in range(0, len(to_rem)):
                    lines.pop(to_rem[i]-i)

                toname = ""                                         #variable for getting named entities                               

                for i in range(1, len(lines)):
                    splitline = re.split(r'\t|\n', lines[i])        #split by either tab or newline -> features list
            
                    if len(splitline) >0:                          #warning: somehow there are many-many different whitespaces in the outcome of the analysis
                                                                    #this len makes sure that there's no indexing error with empty lists
                                                                    #note: the analysis probably makes some trailig whitespaces / tokenizes them anyway
                        self.tok.append((splitline[0]))

                        if len(splitline) >= 6:
                            self.lem.append((splitline[5]))
                            self.morph.append((str(splitline[6])))
                            if str(splitline[7]) == "CONJ":        #quick conversion: emagyar works with a different label
                                self.pos.append(("CCONJ"))
                            else:
                                self.pos.append((str(splitline[7])))
                            self.dep.append((str(splitline[10])))
                            self._head_num.append((str(splitline[11])))
                            self._ids.append((splitline[9], splitline[0]))
                                    
                            if splitline[13] != "O":                                               #ner conversion: emagyar works with a different iob label set
                                if splitline[13][0] == "1":                                        #eliminating standalone label
                                    self.only_ner.append(f"{splitline[0]}\t{splitline[13][2:]}")
                                    self.ner.append((f"B-{splitline[13][2:]}"))
                                elif splitline[13][0] == "E":                                      #eliminating end of NE label
                                    toname = toname + splitline[0]                                  #build up the NE -> put the last part
                                    self.only_ner.append(f"{toname}\t{splitline[13][2:]}")          #NE is ready -> put it in the list
                                    toname = ""                                                     #clear builder variable, new NE will start
                                    self.ner.append((f"I-{splitline[13][2:]}"))                     #append IOB ner as usual, but with I label
                                else:
                                    toname = toname + splitline[0] + " "                            #building the NE because it must be B or I
                                    self.ner.append((splitline[13]))                                #normal append
                            else:
                                self.ner.append((splitline[13]))                                    #normal append, it must be O
                    
                #make dep head list
                self.__make_head_list()
        except Exception as e:
            raise Exception(f"Hiba az e-magyar nyers elemzési fájljának feldolgozásakor: {e}")

            




    def __make_head_list(self):
        #sorts the ids into separate lists per sentences
        ids_per_sentences = []
        i = -1 #always append to the end

        for (head_id, tok) in self._ids:
            #new sentence begins
            if head_id == '1':
                l = []
                ids_per_sentences.append(l)
                i += 1
            ids_per_sentences[i].append((int(head_id), tok))
            #we append a token and an id so we can map that back easily (each token with its own id)
        

        raw_head_tok = self._head_num
        split_rht = []
        prev_len = 0

        for sent in ids_per_sentences:
            curr_len = len(sent)
            split_rht.append(raw_head_tok[prev_len:(prev_len + curr_len)])
            prev_len += curr_len

    



        for (raw_head_list, id_list) in zip(split_rht, ids_per_sentences):
            i = -1
            for (raw_head) in raw_head_list:
                i += 1
                if raw_head == str(0):
                    self.head.append((id_list[i][1])) # as root, itself
                    continue
                for (head_id, tok2) in id_list:
                    if str(raw_head) == str(head_id):
                        self.head.append(tok2)
                        continue
                

            
        


        
            
