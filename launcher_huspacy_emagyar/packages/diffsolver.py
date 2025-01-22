def diffsolver(jj, kk, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, collec_h1, collec_h2, collec_h3, collec_e1, collec_e2):

    modified = False
    if(k+kk < len(e_tokens) and j+jj < len(h_tokens)):
        if(k != len(e_tokens)-kk and j != len(h_tokens)-jj and  h_tokens[j+jj] == e_tokens[k+kk]):
            print(str_to_print(j, k, h_tokens, e_tokens, collec_h1, collec_h2, collec_h3, collec_e1, collec_e2))
            print("_______________________________________________________")
            k = k + 1
            j = j + 1
            if(kk > jj):
                for i in range (0, kk-jj):
                    print("emagyar\t" + diff_to_print_e(k, e_tokens, collec_e1, collec_e2))
                    print("_______________________________________________________")
                    k = k+1
            else:
                for i in range (0, jj-kk):
                    print("huspacy\t" + diff_to_print_h(j, h_tokens, collec_h1, collec_h2, collec_h3))
                    print("_______________________________________________________")
                    j = j+1

            print(str_to_print(j, k, h_tokens, e_tokens, collec_h1, collec_h2, collec_h3, collec_e1, collec_e2))
            print("_______________________________________________________")
            j = j + 1
            k = k + 1
            modified = True

    return j, k, modified

