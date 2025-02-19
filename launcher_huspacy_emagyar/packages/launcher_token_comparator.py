from packages.diffsolver import diffsolver

#what to print with synchronous tokens
def str_to_print(j, k, h_tokens, e_tokens, collec_h1, collec_h2, collec_h3, collec_e1, collec_e2):
    return str(h_tokens[j] == e_tokens[k]) + '\t' + '|' + h_tokens[j] + '|' + '\t' + '|' + e_tokens[k] + '|'

#print emagyar remains in case of tokenization glitch when huspacy is ahead
def diff_to_print_e(k, e_tokens, collec_e1, collec_e2):
    return '\t|' + e_tokens[k] + '|'

#print huspacy remains in case of tokenization glitch when emagyar is ahead
def diff_to_print_h(j, h_tokens, collec_h1, collec_h2, collec_h3):
    return '|' + h_tokens[j] + '|'




def token_comparator(h_tokens, e_tokens):
    l = min(len(h_tokens), len(e_tokens))
    print("huspacy tokenszám: ", len(h_tokens))
    print("e-magyar tokenszám: ", len(e_tokens))

    j = 0
    k = 0
    print("huspacy tokenek \t emagyar tokenek")

    
    while(j != len(h_tokens) and k != len(e_tokens)):
        #normal case: synchronous tokenization
        if(h_tokens[j] == e_tokens[k]):
            print(str_to_print(j, k, h_tokens, e_tokens, None, None, None, None, None))
            print("_______________________________________________________")
            j = j + 1
            k = k + 1
        #abnormal case: tokenization glitch - diffsolving required
        else:
            m = False #modified
            for z in range(1,6):
                if(m):
                    break
                for v in range(1,6):
                    j, k, m = diffsolver(z, v, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, None, None, None, None, None)
                    if(m):
                        break
            if(m):
                continue
            
           
            print(str_to_print(j, k, h_tokens, e_tokens, None, None, None, None, None))
            print("_______________________________________________________")
            j = j + 1
            k = k + 1
     
            break

    #print the remains
    if(j != len(h_tokens)):
        print("huspacy maradek token: ")
        print(h_tokens[j:])
        
    if(k != len(e_tokens)):
        print("emagyar maradek token: ")
        print(e_tokens[k:])


