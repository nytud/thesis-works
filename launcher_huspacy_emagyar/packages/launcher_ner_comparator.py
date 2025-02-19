from packages.diffsolver import diffsolver

#what to print with synchronous tokens
def str_to_print(j, k, h_tokens, e_tokens, h_ners, collec_h2, collec_h3, e_ners, collec_e2):
    return str(h_ners[j] == e_ners[k]) + '\t' +  '|' + h_ners[j] + '|' + '\t' + '|' + e_ners[k] + '|' + "\t\t" + "(" + h_tokens[j] + " " + e_tokens[k] + ")"

#print emagyar remains in case of tokenization glitch when huspacy is ahead
def diff_to_print_e(k, e_tokens, e_ners, collec_e2):
    return '\t\t|' + e_ners[k] + '|'+ "\t\t" + "(" + e_tokens[k] + ")"

#print huspacy remains in case of tokenization glitch when emagyar is ahead
def diff_to_print_h(j, h_tokens, h_ners, collec_h2, collec_h3):
    return '|' + h_ners[j] + '|'+ "\t\t\t" + "(" + h_tokens[j] + ")"


def ner_comparator(h_ners, h_only_ners, e_ners, e_only_ners, h_tokens, e_tokens):
    
    if(len(h_tokens) != len(e_tokens)):
        print("FIGYELEM! Tokenizálásbeli különbség miatt elcsúszás várható!")
        #despite the working diffsolver, the user is warned to look out for anomalies

    l = min(len(h_ners), len(e_ners)) #prevent index error

    j = 0
    k = 0

    #headline
    print("huspacy ner \t emagyar ner")
    
    #iob-printout
    while(j != len(h_ners) and k != len(e_ners)):
        #normal case: synchronous tokenization
        if(h_tokens[j] == e_tokens[k]):
            print(str_to_print(j, k, h_tokens, e_tokens, h_ners, None, None, e_ners, None))
            print("_____________________________________________________")
            j = j + 1
            k = k + 1
        #abnormal case: tokenization glitch - diffsolving required
        else:
            m = False
            for z in range(1,6):
                if(m):
                    break
                for v in range(1,6):
                    j, k, m = diffsolver(z, v, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_ners, None, None, e_ners, None)
                    if(m):
                        break
            if(m):
                continue

            print(str_to_print(j, k, h_tokens, e_tokens, h_ners, None, None, e_ners, None))
            print("_______________________________________________________")
            j = j + 1
            k = k + 1

            break

    #print the remains    
    if(j != len(h_ners)):
        print("huspacy maradek tulajdonnev: ")
        for i in h_ners[j:]:
            print(str(i))
    if(k != len(e_ners)):
        print("emagyar maradek tulajdonnev: ")
        for i in e_ners[j:]:
            print(str(i))
    
    #ner-centered printout from here
    print("////////////////////////////////////////////")
    
    h_dict = {}
    e_dict = {}

    for h in h_only_ners:
        h1 = h.split('\t')[0] #the named entity
        h2 = h.split('\t')[1] #its type
        if(h1 not in h_dict):
            h_dict[h1] = {h2} #add new named entity
        else:
            h_dict[h1].add(h2) #add the new type to the typelist of the existing named entity

    for e in e_only_ners:
        e1 = e.split('\t')[0] #the named entity
        e2 = e.split('\t')[1] #its type
        if(e1 not in e_dict):
            e_dict[e1] = {e2} #add new named entity
        else:
            e_dict[e1].add(e2) #add the new type to the typelist of the existing named entity
    


    only_h = list([]) #the named entity was only found by huspacy
    only_e = list([]) #the named entity was only found by emagyar
    #matching the emagyar entities to huspacy entities
    for (kh, vh) in h_dict.items():
        if(kh in e_dict): #found corresponding entity
            print(str(vh == e_dict[kh]) + '\t' + kh + '\t' + str(vh) + '\t' + str(e_dict[kh])) #comparing
        else:
            only_h.append(kh + '\t' + str(vh)) #not found corresponding entity
    
    #matching the huspacy entities to emagyar entities
    for (ke, ve) in e_dict.items():
        if(ke not in h_dict):
            only_e.append(ke + '\t' + str(ve)) #only not found check is enough because the intersection had to be handled from the huspacy side already

    #print the remains
    print("huspacy maradek:")
    for h in only_h:
        print(h)

    print("emagyar maradek:")
    for e in only_e:
        print(e)
    

