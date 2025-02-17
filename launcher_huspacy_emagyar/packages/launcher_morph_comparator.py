from packages.diffsolver import diffsolver

#what to print with synchronous tokens
def str_to_print(j, k, h_tokens, e_tokens, h_udmorph, h_emm, collec_h3, e_morph, collec_e2):
    return str(h_emm[j] == e_morph[k]) + '\t' + '|' + h_udmorph[j] + '|' + '\t' + '|' + h_emm[j] + '|' + '\t' + '|' + e_morph[k] + '|' + "\t\t" + "(" + h_tokens[j] + " " + e_tokens[k] + ")"

#print emagyar remains in case of tokenization glitch when huspacy is ahead
def diff_to_print_e(k, e_tokens, e_morph, collec_e2):
    return '\t\t|' + e_morph[k] + '|' + "\t\t" + "(" + e_tokens[k] + ")"

#print huspacy remains in case of tokenization glitch when emagyar is ahead
def diff_to_print_h(j, h_tokens, h_udmorph, h_emm, collec_h3):
    return '|' + h_udmorph[j] + '|' + '\t' + '|' + h_emm[j] + '|' + "\t\t\t" + "(" + h_tokens[j] + ")"



def morph_comparator(h_udmorph, h_emm, e_morph, h_tokens, e_tokens):
    if(len(h_tokens) != len(e_tokens)):
        print("FIGYELEM! Tokenizálásbeli különbség miatt elcsúszás várható!")
        #despite the working diffsolver, the user is warned to look out for anomalies

    l = min(len(h_udmorph), len(h_emm), len(e_morph)) #prevent index error

    j = 0
    k = 0

    #headline
    print("huspacy ud \t huspacy emmorph \t emagyar morph")
    
    while(j != len(h_tokens) and k != len(e_tokens)):
        #normal case: synchronous tokenization
        if(h_tokens[j] == e_tokens[k]):
            print(str_to_print(j, k, h_tokens, e_tokens, h_udmorph, h_emm, None, e_morph, None))
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
                    j, k, m = diffsolver(z, v, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_udmorph, h_emm, None, e_morph, None)
                    if(m):
                        break
            if(m):
                continue

            print(str_to_print(j, k, h_tokens, e_tokens, h_udmorph, h_emm, None, e_morph, None))
            print("_______________________________________________________")
            j = j + 1
            k = k + 1

            break

    #print the remains   
    if(j != len(h_emm)):
        print("huspacy maradek lemma: ")
        print(h_udmorph[j:])
        print(h_emm[j:])
    
    if(k != len(e_morph)):
        print("emagyar maradek lemma: ")
        print(e_morph[k:])





