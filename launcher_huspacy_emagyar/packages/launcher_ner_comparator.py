from packages.diffsolver import diffsolver

def str_to_print(j, k, h_tokens, e_tokens, h_ners, collec_h2, collec_h3, e_ners, collec_e2):
    return str(h_ners[j] == e_ners[k]) + '\t' +  '|' + h_ners[j] + '|' + '\t' + '|' + e_ners[k] + '|' + "\t\t" + "(" + h_tokens[j] + " " + e_tokens[k] + ")"

def diff_to_print_e(k, e_tokens, e_ners, collec_e2):
    return '\t\t|' + e_ners[k] + '|'+ "\t\t" + "(" + e_tokens[k] + ")"


def diff_to_print_h(j, h_tokens, h_ners, collec_h2, collec_h3):
    return '|' + h_ners[j] + '|'+ "\t\t\t" + "(" + h_tokens[j] + ")"


def ner_comparator(h_ners, h_only_ners, e_ners, e_only_ners, h_tokens, e_tokens):
    
    if(len(h_tokens) != len(e_tokens)):
        print("FIGYELEM! Tokenizálásbeli különbség miatt elcsúszás várható!")

    l = min(len(h_ners), len(e_ners))

    j = 0
    k = 0

    print("huspacy ner \t emagyar lemma")

    hsplit = list(map(lambda x: x.split(), h_only_ners))
    esplit = list(map(lambda x: x.split(), e_only_ners))

    h_names = [h[0] for h in hsplit]
    e_names = [e[0] for e in esplit]
    

    while(j != len(h_ners) and k != len(e_ners)):
        
        #if(hsplit[j][0] == esplit[k][0]):
        if(h_tokens[j] == e_tokens[k]):
            print(str_to_print(j, k, h_tokens, e_tokens, h_ners, None, None, e_ners, None))
            print("_____________________________________________________")
            j = j + 1
            k = k + 1
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

        
    if(j != len(h_ners)):
        print("huspacy maradek tulajdonnev: ")
        for i in h_ners[j:]:
            print(str(i))
    if(k != len(e_ners)):
        print("emagyar maradek tulajdonnev: ")
        for i in e_ners[j:]:
            print(str(i))
    

    print("////////////////////////////////////////////")
    
    h_dict = {}
    e_dict = {}

    for h in h_only_ners:
        h1 = h.split('\t')[0]
        h2 = h.split('\t')[1]
        if(h1 not in h_dict):
            h_dict[h1] = {h2}
        else:
            h_dict[h1].add(h2)

    for e in e_only_ners:
        e1 = e.split('\t')[0]
        e2 = e.split('\t')[1]
        if(e1 not in e_dict):
            e_dict[e1] = {e2}
        else:
            e_dict[e1].add(e2)
    


    only_h = list([])
    only_e = list([])
    for (kh, vh) in h_dict.items():
        if(kh in e_dict):
            print(str(vh == e_dict[kh]) + '\t' + kh + '\t' + str(vh) + '\t' + str(e_dict[kh]))
        else:
            only_h.append(kh + '\t' + str(vh))
    
    for (ke, ve) in e_dict.items():
        if(ke not in h_dict):
            only_e.append(ke + '\t' + str(ve))

    print("huspacy maradek:")
    for h in only_h:
        print(h)

    print("emagyar maradek:")
    for e in only_e:
        print(e)
    

