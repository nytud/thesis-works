from packages.diffsolver import diffsolver

#what to print with synchronous tokens
def str_to_print(j, k, h_tokens, e_tokens, h_pos, h_tag, h_udpos, e_pos, collec_e2):
    return str(h_pos[j] == e_pos[k] == h_tag[j] == h_udpos[j]) + '\t' + '|' + h_pos[j] + '|' + '\t' + '|' + h_tag[j] + '|' + '\t' + '|' + str(h_udpos[j]) + '|' + '\t' + '|' + e_pos[k] + '|' + "\t\t" + "(" + h_tokens[j] + " " + e_tokens[k] + ")"

#print emagyar remains in case of tokenization glitch when huspacy is ahead
def diff_to_print_e(k, e_tokens, e_pos, collec_e2):
    return '\t\t|' + e_pos[k] + '|' + "\t\t" + "(" + e_tokens[k] + ")"

#print huspacy remains in case of tokenization glitch when emagyar is ahead
def diff_to_print_h(j, h_tokens, h_pos, h_tag, h_udpos):
    return '|' + h_pos[j] + '|' + "\t" + '|' + h_tag[j] + '|' + "\t" + '|' + str(h_udpos[j]) + '|' + "\t\t\t" + "(" + h_tokens[j] + ")"


def pos_comparator(h_pos, h_tag, h_udpos, e_pos, h_tokens, e_tokens):
    if(len(h_tokens) != len(e_tokens)):
        print("FIGYELEM! Tokenizálásbeli különbség miatt elcsúszás várható!")
        #despite the working diffsolver, the user is warned to look out for anomalies

    l = min(len(h_pos), len(h_tag), len(h_udpos), len(e_pos)) #prevent index error

    j = 0
    k = 0

    #headline
    print("huspacy pos (sima upos) \t huspacy tag (detailed pos) \t huspacy em ud tag \t emagyar pos")

    while(j != len(h_tokens) and k != len(e_tokens)):
        #normal case: synchronous tokenization
        if(h_tokens[j] == e_tokens[k]):
            print(str_to_print(j, k, h_tokens, e_tokens, h_pos, h_tag, h_udpos, e_pos, None))
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
                    j, k, m = diffsolver(z, v, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_pos, h_tag, h_udpos, e_pos, None)
                    if(m):
                        break
            if(m):
                continue

            print(str_to_print(j, k, h_tokens, e_tokens, h_pos, h_tag, h_udpos, e_pos, None))
            print("_______________________________________________________")
            j = j + 1
            k = k + 1

            break

    #print the remains  
    if(j != len(h_pos)):
        print("huspacy maradek pos: ")
        print(h_pos[j:])
        print(h_tag[j:])
        print(h_udpos[j:])
    if(k != len(e_pos)):
        print("emagyar maradek lemma: ")
        print(e_pos[k:])


