from packages.diffsolver import diffsolver

def str_to_print(j, k, h_tokens, e_tokens, h_lems, h_lems_em, collec_h3, e_lems, collec_e2):
    return str(h_lems[j] == e_lems[k] == h_lems_em[j]) + '\t' + '|' + h_lems[j] + '|' + '\t' + '|' + str(h_lems_em[j]) + '|' + '\t' + '|' + e_lems[k] + '|' + "\t\t" + "(" + h_tokens[j] + " " + e_tokens[k] + ")"


def diff_to_print_e(k, e_tokens, e_lems, collec_e2):
    return '\t\t|' + e_lems[k] + '|' + "\t\t" + "(" + e_tokens[k] + ")"


def diff_to_print_h(j, h_tokens, h_lems, h_lems_em, collec_h3):
    return '|' + h_lems[j] + '|' + "\t" + '|' + str(h_lems_em[j]) + '|' + "\t\t\t" + "(" + h_tokens[j] + ")"


def lemma_comparator(h_lems, h_lems_em, e_lems, h_tokens, e_tokens):
    if(len(h_tokens) != len(e_tokens)):
        print("FIGYELEM! Tokenizálásbeli különbség miatt elcsúszás várható!")

    l = min(len(h_lems), len(e_lems))

    j = 0
    k = 0

    print("huspacy lemma \t huspacy em_lemma \t emagyar lemma")

    while(j != len(h_tokens) and k != len(e_tokens)):
        if(h_tokens[j] == e_tokens[k]):
            print(str_to_print(j, k, h_tokens, e_tokens, h_lems, h_lems_em, None, e_lems, None))
            print("_____________________________________________________")
            j = j + 1
            k = k + 1
        else:
            j, k, m = diffsolver(2, 1, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_lems, h_lems_em, None, e_lems, None)
            if(m):
                continue
            j, k, m = diffsolver(1, 2, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_lems, h_lems_em, None, e_lems, None)
            if(m):
                continue
            j, k, m = diffsolver(3, 1, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_lems, h_lems_em, None, e_lems, None)
            if(m):
                continue
            j, k, m = diffsolver(1, 3, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_lems, h_lems_em, None, e_lems, None)
            if(m):
                continue
            j, k, m = diffsolver(4, 1, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_lems, h_lems_em, None, e_lems, None)
            if(m):
                continue
            j, k, m = diffsolver(1, 4, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_lems, h_lems_em, None, e_lems, None)
            if(m):
                continue
            j, k, m = diffsolver(5, 1, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_lems, h_lems_em, None, e_lems, None)
            if(m):
                continue
            j, k, m = diffsolver(1, 5, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_lems, h_lems_em, None, e_lems, None)
            if(m):
                continue
            j, k, m = diffsolver(3, 2, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_lems, h_lems_em, None, e_lems, None)
            if(m):
                continue
            j, k, m = diffsolver(2, 3, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_lems, h_lems_em, None, e_lems, None)
            if(m):
                continue
            j, k, m = diffsolver(4, 3, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_lems, h_lems_em, None, e_lems, None)
            if(m):
                continue
            j, k, m = diffsolver(3, 4, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_lems, h_lems_em, None, e_lems, None)
            if(m):
                continue
            j, k, m = diffsolver(4, 2, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_lems, h_lems_em, None, e_lems, None)
            if(m):
                continue
            j, k, m = diffsolver(2, 4, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_lems, h_lems_em, None, e_lems, None)
            if(m):
                continue
            j, k, m = diffsolver(1, 1, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_lems, h_lems_em, None, e_lems, None)
            if(m):
                continue
            j, k, m = diffsolver(2, 2, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_lems, h_lems_em, None, e_lems, None)
            if(m):
                continue
            j, k, m = diffsolver(3, 3, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_lems, h_lems_em, None, e_lems, None)
            if(m):
                continue

            print(str_to_print(j, k, h_tokens, e_tokens, h_lems, h_lems_em, None, e_lems, None))
            print("_______________________________________________________")
            j = j + 1
            k = k + 1

            break

        
    if(j != len(h_lems)):
        print("huspacy maradek lemma: ")
        print(h_lems[j:])
        print(h_lems_em[j:])
    if(k != len(e_lems)):
        print("emagyar maradek lemma: ")
        print(e_lems[k:])


