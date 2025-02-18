def diffsolver(jj, kk, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, collec_h1, collec_h2, collec_h3, collec_e1, collec_e2):

    modified = False
    if(k+kk < len(e_tokens) and j+jj < len(h_tokens)): #prevent index error
        if(k != len(e_tokens)-kk and j != len(h_tokens)-jj and  h_tokens[j+jj] == e_tokens[k+kk]): #found the next match
            print(str_to_print(j, k, h_tokens, e_tokens, collec_h1, collec_h2, collec_h3, collec_e1, collec_e2)) #we print it as usual, because it is a match
            print("_______________________________________________________")
            k = k + 1
            j = j + 1
            if(kk > jj): #emagyar shift was greater -> huspacy is ahead -> emagyar remains are to be printed
                for i in range (0, kk-jj):
                    print("emagyar\t" + diff_to_print_e(k, e_tokens, collec_e1, collec_e2))
                    print("_______________________________________________________")
                    k = k+1
            else:
                for i in range (0, jj-kk): #huspacy shift was greater -> emagyar is ahead -> huspacy remains are to be printed
                    print("huspacy\t" + diff_to_print_h(j, h_tokens, collec_h1, collec_h2, collec_h3))
                    print("_______________________________________________________")
                    j = j+1

            print(str_to_print(j, k, h_tokens, e_tokens, collec_h1, collec_h2, collec_h3, collec_e1, collec_e2)) #have to resume teh printout as normal
            print("_______________________________________________________")
            j = j + 1
            k = k + 1
            modified = True #means: the diffsolving is done, the original print has been modified accordingly
            #False only when diffsolver was called with wrong shift combination

    return j, k, modified

