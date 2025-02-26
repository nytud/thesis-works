import docker
import tarfile
import io

class Emagyar:
    def __init__(self):
        self.tok = list([])
        self.morph = list([])
        self.lem = list([])
        self.pos = list([])
        self.dep = list([])
        self.head = list([])
        self.ner = list([])
        self.only_ner = list([])

    def run(self, fname, txt):
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
                with open('eredmeny5.tar', 'wb') as f:
                    strm, status = container.get_archive("/app/ana_emagyar_" + fname) #get the result from docker
        
                    #transfer its contents to a local tar file
                    for chunk in strm:
                        f.write(chunk)
                

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

        self.__makelists(fname)


    def print(self, fname):
        with open('./eredmenyek/huspacy/ana_emagyar_' + fname, 'r') as f:
            print(f.read())

    def __makelists(self, fname):
        pass
    
        
