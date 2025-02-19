def emagyar(txt, fname, oute, e_tokens, e_lems, e_morph, e_ners, e_only_ners, e_pos, e_dep, e_head):
    import docker
    import tarfile
    import io

    #run emagyar through docker
    client = docker.from_env()
    container = client.containers.run('mtaril/emtsv', detach=True)

    tar_stream = io.BytesIO()

    with tarfile.open(fileobj=tar_stream, mode='w') as tar:
        tar.add("currentinput.txt") #we transfer the input as a file -> this makes a tarfile out of it

    tar_stream.seek(0)
    succ = container.put_archive(path='/app', data=tar_stream) #transfering the input file to docker

    if(succ): #transfer was successful
        #run emagyar in the docker
        command = "python3 ./main.py tok,spell,morph,pos,conv-morph,dep,chunk,ner -i ./currentinput.txt -o ana_emagyar_" + fname
        result = container.exec_run(command)

        if(result.exit_code == 0):
            f = open('eredmeny5.tar', 'wb')
            strm, status = container.get_archive("/app/ana_emagyar_" + fname) #get the result from docker
        
            #transfer its contents to a local tar file
            for chunk in strm:
                f.write(chunk)
            f.close()

            #get the real contents from the tar file and put it to the designated directory
            with tarfile.open('eredmeny5.tar', 'r') as tar:
                tar.extractall('./eredmenyek/emagyar')

        else:
            print("sikertelen elemzes, nem jott letre outputfile!")
            print(result)

    #cleaning up the container
    container.stop()
    print("container stopped")
    container.remove()
    print("container removed")

    #if oute is configured, print out the results
    if(oute):
        f = open('./eredmenyek/emagyar/ana_emagyar_' + fname, 'r')
        print(f.read())
        f.close()

    #prepare stateholder lists for comparation
    e_tokens, e_lems, e_morph, e_ners, e_only_ners, e_pos, e_dep, e_head = makelists(fname, e_tokens, e_lems, e_morph, e_ners, e_only_ners, e_pos, e_dep, e_head)

    return e_tokens, e_lems, e_morph, e_ners, e_only_ners, e_pos, e_dep, e_head






def makelists(fname, e_tokens, e_lems, e_morph, e_ners, e_only_ners, e_pos, e_dep, e_head):
    #emagyar gave us the results in its own format -> we have to process and transform it to work with it like we would with huspacy
    f2 = open('./eredmenyek/emagyar/ana_emagyar_' + fname)
    lines_raw = f2.read()
    lines = lines_raw.split('\n')

    #remove empty lines
    to_rem = list([])

    for i in range(0, len(lines)):
        if(len(lines[i]) == 0):
            to_rem.append(i)

    for i in range(0, len(to_rem)):
        lines.pop(to_rem[i]-i)

    import re

    toname = "" #variable for getting named entities
    ids = list([]) #every token has an id in the sentence it is in for dependency
    e_head_num = list([]) #this links the dep head by id

    for i in range(1, len(lines)):
        splitline = re.split(r'\t|\n', lines[i]) #split by either tab or newline -> features list
        
        if(len(splitline) >0):#warning: somehow there are many-many different whitespaces in the outcome of the analysis
            #this len makes sure that there's no indexing error with empty lists
            #note: the analysis probably makes some trailig whitespaces / tokenizes them anyway
            e_tokens.append(splitline[0])

            if(len(splitline) >= 6):
                e_lems.append(splitline[5])
                e_morph.append(str(splitline[6]))
                if(str(splitline[7]) == "CONJ"):  #quick conversion: emagyar works with a different label
                    e_pos.append("CCONJ")
                else:
                    e_pos.append(str(splitline[7]))
                e_dep.append(str(splitline[10]))
                e_head_num.append(str(splitline[11]))
                ids.append((splitline[9], splitline[0]))
                
                
                if(splitline[13] != 'O'): #ner conversion: emagyar works with a different iob label set
                    if(splitline[13][0] == "1"): #eliminating standalone label
                        e_only_ners.append(splitline[0] + '\t' + splitline[13][2:])
                        e_ners.append("B-" + splitline[13][2:])
                    elif(splitline[13][0] == "E"): #eliminating end of NE label
                        toname = toname + splitline[0] #build up the NE -> put the last part
                        e_only_ners.append(toname + '\t' + splitline[13][2:]) #NE is ready -> put it in the list
                        toname = "" #clear builder variable, new NE will start
                        e_ners.append("I-" + splitline[13][2:]) #append IOB ner as usual, but with I label
                    else:
                        toname = toname + splitline[0] + " " #building the NE because it must be B or I
                        e_ners.append(splitline[13]) #normal append
                else:
                    e_ners.append(splitline[13]) #normal append, it must be O
                
    #make dep head list
    make_head_list(ids, e_head_num, e_dep, e_head, e_tokens)
    

    f2.close()

    return e_tokens, e_lems, e_morph, e_ners, e_only_ners, e_pos, e_dep, e_head






def make_head_list(ids, e_head_num, e_dep, e_head, e_tokens):
    #sorts the ids into separate lists per sentences
    ids_per_sentences = list([])
    i = -1

    for (id, tok) in ids:
        if(id == '1'):#new sentence begins
            l = list([])
            ids_per_sentences.append(l)
            i += 1
        ids_per_sentences[i].append((int(id), tok))#we append a token and an id so we can map that back easily (each token with its own id)

    i = 0#which sentence (sublist) are we in
    move = False#should we switch sentence (sublist)
    for j in range(0, len(e_head_num)):#iterating through the raw headlist
        h = int(e_head_num[j])#get the raw head

        if(move and h == 0 and i < len(ids_per_sentences)-1):#we are at the second zero, aka the . (note: emagyar can make mistakes (on specifiy cases) in this, so that's not 100% certain)
            i += 1
            move = False
        
        if(e_dep[j] == 'ROOT'):
            move = True#if root found, we have to move when the next 0 hits
            #note: somehow only the sentence terminating puntcuation mark gets 0, so other punctuation chars get decent phrase ids
        if(h == 0):
            e_head.append(e_tokens[j])
            #e_head.append("")
        else:
            for (id, tok) in ids_per_sentences[i]:
                if(h == id):
                    e_head.append(tok)
                    #print(i, tok)
                    break






            
 

    

    

