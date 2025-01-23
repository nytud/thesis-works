from packages.diffsolver import diffsolver
from packages.dep_converter import convert

def str_to_print(j, k, h_tokens, e_tokens, h_dep, h_head, collec_h3, e_dep, e_head):
    return str(convert(h_dep[j]) == e_dep[k]) + "\t" +  str(str(h_head[j]) == str(e_head[k])) + '\t' + '|(' + h_dep[j] + ')|' + "\t" + '|' + convert(h_dep[j]) + '|' + '\t' + '|' + str(h_head[j]) + '|' + '\t' + '|' + e_dep[k] + '|' + '\t' + '|' + e_head[k] + '|' + "\t\t" + "(" + h_tokens[j] + " " + e_tokens[k] + ")"


def diff_to_print_e(k, e_tokens, e_dep, e_head):
    return '\t\t|' + e_dep[k] + '|' + '\t\t|' + e_head[k] + '|' + "\t\t" + "(" + e_tokens[k] + ")"


def diff_to_print_h(j, h_tokens, h_dep, h_head, collec_h3):
    return '\t|' + h_dep[j] + '|' + "\t" + "converted as: " + convert(h_dep[j]) + "\t" + '|' + str(h_head[j]) + '|' + "\t\t\t" + "(" + h_tokens[j] + ")"


def dep_comparator(h_dep, h_head, e_dep, e_head, h_tokens, e_tokens):
    if(len(h_tokens) != len(e_tokens)):
        print("FIGYELEM! Tokenizálásbeli különbség miatt elcsúszás várható!")

    l = min(len(h_dep), len(h_head), len(e_dep), len(e_head))

    j = 0
    k = 0

    print("huspacy dep \t huspacy head \t emagyar dep \t emagyar head")

    while(j != len(h_tokens) and k != len(e_tokens)):
        if(h_tokens[j] == e_tokens[k]):
            print(str_to_print(j, k, h_tokens, e_tokens, h_dep, h_head, None, e_dep, e_head))
            print("_____________________________________________________")
            j = j + 1
            k = k + 1
        else:
            j, k, m = diffsolver(2, 1, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_dep, h_head, None, e_dep, e_head)
            if(m):
                continue
            j, k, m = diffsolver(1, 2, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_dep, h_head, None, e_dep, e_head)
            if(m):
                continue
            j, k, m = diffsolver(3, 1, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_dep, h_head, None, e_dep, e_head)
            if(m):
                continue
            j, k, m = diffsolver(1, 3, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_dep, h_head, None, e_dep, e_head)
            if(m):
                continue
            j, k, m = diffsolver(4, 1, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_dep, h_head, None, e_dep, e_head)
            if(m):
                continue
            j, k, m = diffsolver(1, 4, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_dep, h_head, None, e_dep, e_head)
            if(m):
                continue
            j, k, m = diffsolver(5, 1, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_dep, h_head, None, e_dep, e_head)
            if(m):
                continue
            j, k, m = diffsolver(1, 5, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_dep, h_head, None, e_dep, e_head)
            if(m):
                continue
            j, k, m = diffsolver(3, 2, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_dep, h_head, None, e_dep, e_head)
            if(m):
                continue
            j, k, m = diffsolver(2, 3, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_dep, h_head, None, e_dep, e_head)
            if(m):
                continue
            j, k, m = diffsolver(4, 3, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_dep, h_head, None, e_dep, e_head)
            if(m):
                continue
            j, k, m = diffsolver(3, 4, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_dep, h_head, None, e_dep, e_head)
            if(m):
                continue
            j, k, m = diffsolver(4, 2, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_dep, h_head, None, e_dep, e_head)
            if(m):
                continue
            j, k, m = diffsolver(2, 4, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_dep, h_head, None, e_dep, e_head)
            if(m):
                continue
            j, k, m = diffsolver(1, 1, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_dep, h_head, None, e_dep, e_head)
            if(m):
                continue
            j, k, m = diffsolver(2, 2, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_dep, h_head, None, e_dep, e_head)
            if(m):
                continue
            j, k, m = diffsolver(3, 3, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, h_dep, h_head, None, e_dep, e_head)
            if(m):
                continue

            print(str_to_print(j, k, h_tokens, e_tokens, h_dep, h_head, None, e_dep, e_head))
            print("_______________________________________________________")
            j = j + 1
            k = k + 1

            break

        
    if(j != len(h_dep)):
        print("huspacy maradek pos: ")
        print(h_dep[j:])
        print(h_head[j:])
    
    if(k != len(e_dep)):
        print("emagyar maradek lemma: ")
        print(e_pos[k:])
        print(e_head[k:])


