from packages.diffsolver import diffsolver

#what to print with synchronous tokens
def str_to_print(j, k, h_tokens, e_tokens, h_lems, h_lems_em, collec_h3, e_lems, collec_e2):
    return str(h_lems[j] == e_lems[k] == h_lems_em[j]) + '\t' + '|' + h_lems[j] + '|' + '\t' + '|' + str(h_lems_em[j]) + '|' + '\t' + '|' + e_lems[k] + '|' + "\t\t" + "(" + h_tokens[j] + " " + e_tokens[k] + ")"

#print emagyar remains in case of tokenization glitch when huspacy is ahead
def diff_to_print_e(k, e_tokens, e_lems, collec_e2):
    return '\t\t|' + e_lems[k] + '|' + "\t\t" + "(" + e_tokens[k] + ")"

#print huspacy remains in case of tokenization glitch when emagyar is ahead
def diff_to_print_h(j, h_tokens, h_lems, h_lems_em, collec_h3):
    return '|' + h_lems[j] + '|' + "\t" + '|' + str(h_lems_em[j]) + '|' + "\t\t\t" + "(" + h_tokens[j] + ")"


def lemma_comparator(h_lems, h_lems_em, e_lems, h_tokens, e_tokens):
    if(len(h_tokens) != len(e_tokens)):
        print("FIGYELEM! Tokenizálásbeli különbség miatt elcsúszás várható!")
        #despite the working diffsolver, the user is warned to look out for anomalies

    l = min(len(h_lems), len(e_lems)) #prevent index error

    j = 0
    k = 0

    #headline
    print("huspacy lemma \t huspacy em_lemma \t emagyar lemma")

    while(j != len(h_tokens) and k != len(e_tokens)):
        #normal case: synchronous tokenization
        if(h_tokens[j] == e_tokens[k]):
            print(str_to_print(j, k, h_tokens, e_tokens, h_lems, h_lems_em, None, e_lems, None))
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
                    j, k, m = diffsolver(z, v, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_lems, h_lems_em, None, e_lems, None)
                    if(m):
                        break
            if(m):
                continue
            

            print(str_to_print(j, k, h_tokens, e_tokens, h_lems, h_lems_em, None, e_lems, None))
            print("_______________________________________________________")
            j = j + 1
            k = k + 1

            break


    #print the remains    
    if(j != len(h_lems)):
        print("huspacy maradek lemma: ")
        print(h_lems[j:])
        print(h_lems_em[j:])
    if(k != len(e_lems)):
        print("emagyar maradek lemma: ")
        print(e_lems[k:])


