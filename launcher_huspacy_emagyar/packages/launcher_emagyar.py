def emagyar(txt, fname, oute, e_tokens, e_lems, e_morph, e_ners, e_only_ners, e_pos, e_dep, e_head):
    import docker
    import tarfile
    import io

    client = docker.from_env()
    container = client.containers.run('mtaril/emtsv', detach=True)

    tar_stream = io.BytesIO()

    with tarfile.open(fileobj=tar_stream, mode='w') as tar:
        tar.add("currentinput.txt")

    tar_stream.seek(0)
    succ = container.put_archive(path='/app', data=tar_stream)

    if(succ):
        command = "python3 ./main.py tok,spell,morph,pos,conv-morph,dep,chunk,ner -i ./currentinput.txt -o ana_emagyar_" + fname
        result = container.exec_run(command)

        if(result.exit_code == 0):
            f = open('eredmeny5.tar', 'wb')
            strm, status = container.get_archive("/app/ana_emagyar_" + fname)
        
            for chunk in strm:
                f.write(chunk)
            f.close()

            with tarfile.open('eredmeny5.tar', 'r') as tar:
                tar.extractall('./eredmenyek/emagyar')

        else:
            print("sikertelen elemzes, nem jott letre outputfile!")
            print(result)

    container.stop()
    print("container stopped")
    container.remove()
    print("container removed")


    if(oute):
        f = open('./eredmenyek/emagyar/ana_emagyar_' + fname, 'r')
        print(f.read())
        f.close()


    e_tokens, e_lems, e_morph, e_ners, e_only_ners, e_pos, e_dep, e_head = makelists(fname, e_tokens, e_lems, e_morph, e_ners, e_only_ners, e_pos, e_dep, e_head)

    return e_tokens, e_lems, e_morph, e_ners, e_only_ners, e_pos, e_dep, e_head






def makelists(fname, e_tokens, e_lems, e_morph, e_ners, e_only_ners, e_pos, e_dep, e_head):
    f2 = open('./eredmenyek/emagyar/ana_emagyar_' + fname)
    lines_raw = f2.read()
    lines = lines_raw.split('\n')

    to_rem = list([])

    for i in range(0, len(lines)):
        if(len(lines[i]) == 0):
            to_rem.append(i)

    for i in range(0, len(to_rem)):
        lines.pop(to_rem[i]-i)

    import re

    toname = ""
    ids = list([])
    
    e_head_num = list([])
    for i in range(1, len(lines)):
        splitline = re.split(r'\t|\n', lines[i])
        #print(toname)
        if(len(splitline) >0):#warning: somehow there are many-many different whitespaces in the outcome of the analysis
            #this len makes sure that there's no indexing error with empty lists
            #note: maybe (well, probably) the analysis makes some trailig whitespaces / tokenizes them anyway, we can't know for sure :(
            e_tokens.append(splitline[0])

            if(len(splitline) >= 6):
                e_lems.append(splitline[5])
                e_morph.append(str(splitline[6]))
                if(str(splitline[7]) == "CONJ"):
                    e_pos.append("CCONJ")
                else:
                    e_pos.append(str(splitline[7]))
                e_dep.append(str(splitline[10]))
                e_head_num.append(str(splitline[11]))
                ids.append((splitline[9], splitline[0]))
                #e_ners.append(splitline[13])
                
                if(splitline[13] != 'O'):#ner
                    if(splitline[13][0] == "1"):
                        e_only_ners.append(splitline[0] + '\t' + splitline[13][2:])
                        e_ners.append("B-" + splitline[13][2:])
                    elif(splitline[13][0] == "E"):
                        toname = toname + splitline[0]
                        e_only_ners.append(toname + '\t' + splitline[13][2:])
                        toname = ""
                        e_ners.append("I-" + splitline[13][2:])
                    else:
                        toname = toname + splitline[0] + " "
                        e_ners.append(splitline[13])
                else:
                    e_ners.append(splitline[13])
                

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

        if(move and h == 0 and i < len(ids_per_sentences)-1):#we are at the second zero, aka the . NOOOO that's not certain
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





def dep_converter(e_dep):
    pass
            
 

    

    

