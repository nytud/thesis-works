from packages.diffsolver import diffsolver
from packages.dep_converter import convert

#what to print with synchronous tokens
def str_to_print(j, k, h_tokens, e_tokens, h_dep, h_head, collec_h3, e_dep, e_head):
    return str(convert(h_dep[j]) == e_dep[k]) + "\t" +  str(str(h_head[j]) == str(e_head[k])) + '\t' + '|(' + h_dep[j] + ')|' + "\t" + '|' + convert(h_dep[j]) + '|' + '\t' + '|' + str(h_head[j]) + '|' + '\t' + '|' + e_dep[k] + '|' + '\t' + '|' + e_head[k] + '|' + "\t\t" + "(" + h_tokens[j] + " " + e_tokens[k] + ")"

#print emagyar remains in case of tokenization glitch when huspacy is ahead
def diff_to_print_e(k, e_tokens, e_dep, e_head):
    return '\t\t|' + e_dep[k] + '|' + '\t\t|' + e_head[k] + '|' + "\t\t" + "(" + e_tokens[k] + ")"

#print huspacy remains in case of tokenization glitch when emagyar is ahead
def diff_to_print_h(j, h_tokens, h_dep, h_head, collec_h3):
    return '\t|' + h_dep[j] + '|' + "\t" + "converted as: " + convert(h_dep[j]) + "\t" + '|' + str(h_head[j]) + '|' + "\t\t\t" + "(" + h_tokens[j] + ")"


def dep_comparator(h_dep, h_head, e_dep, e_head, h_tokens, e_tokens):
    if(len(h_tokens) != len(e_tokens)):
        print("FIGYELEM! Tokenizálásbeli különbség miatt elcsúszás várható!")
        #despite the working diffsolver, the user is warned to look out for anomalies

    l = min(len(h_dep), len(h_head), len(e_dep), len(e_head)) #prevent index error

    j = 0
    k = 0


    #headline
    print("huspacy dep \t huspacy head \t emagyar dep \t emagyar head")

    while(j != len(h_tokens) and k != len(e_tokens)):
        #normal case: synchronous tokenization
        if(h_tokens[j] == e_tokens[k]):
            print(str_to_print(j, k, h_tokens, e_tokens, h_dep, h_head, None, e_dep, e_head))
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
                    j, k, m = diffsolver(z, v, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_dep, h_head, None, e_dep, e_head)
                    if(m):
                        break
            if(m):
                continue
            

            print(str_to_print(j, k, h_tokens, e_tokens, h_dep, h_head, None, e_dep, e_head))
            print("_______________________________________________________")
            j = j + 1
            k = k + 1

            break


    #print the remains  
    if(j != len(h_dep)):
        print("huspacy maradek pos: ")
        print(h_dep[j:])
        print(h_head[j:])
    
    if(k != len(e_dep)):
        print("emagyar maradek lemma: ")
        print(e_dep[k:])
        print(e_head[k:])


