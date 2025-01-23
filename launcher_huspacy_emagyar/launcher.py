import sys
import glob
from packages.launcher_emagyar import emagyar
from packages.launcher_huspacy import huspacy
from packages.launcher_token_comparator import token_comparator
from packages.launcher_morph_comparator import morph_comparator
from packages.launcher_lemma_comparator import lemma_comparator
from packages.launcher_ner_comparator import ner_comparator
from packages.launcher_pos_comparator import pos_comparator
from packages.launcher_dep_comparator import dep_comparator



args = sys.argv[1:]

if len(args) == 0:
    sys.exit("Nincs parameter!")

oute = False
outh = False
is_emagyar = False
is_huspacy = False
tok_comp = False
morph_comp = False
lem_comp = False
ner_comp = False
pos_comp = False
dep_comp = False


if("-emagyar" in list(args)):
    is_emagyar = True

if("-huspacy" in list(args)):
    is_huspacy = True

if("-oute" in list(args)):
    oute = True

if("-outh" in list(args)):
    outh = True

if("-tok" in list(args)):
    tok_comp = True

if("-morph" in list(args)):
    morph_comp = True

if("-lem" in list(args)):
    lem_comp = True

if("-ner" in list(args)):
    ner_comp = True

if("-pos" in list(args)):
    pos_comp = True

if("-dep" in list(args)):
    dep_comp = True



files = list([])
h_tokens = list([])
e_tokens = list([])
h_lems = list([])
h_lems_em = list([])
e_lems = list([])
h_udmorph = list([])
h_emm = list([])
e_morph = list([])
h_ners = list([])
h_only_ners = list([])
e_ners = list([])
e_only_ners = list([])
h_pos = list([])
h_tag = list([])
h_udpos = list([])
e_pos = list([])
h_dep = list([])
h_head = list([])
e_dep = list([])
e_head = list([])

for a in args:
    if(a[-4:] == ".txt"):
        files = files + glob.glob(a)
    elif(a == "-emagyar" 
            or a == "-huspacy" 
            or a == "-oute" 
            or a == "-outh"
            or a == "-tok"
            or a == "-morph"
            or a == "-lem"
            or a == "-ner"
            or a == "-pos"
            or a == "-dep"):
        pass
    else:
        sys.exit("Hiba: ismeretlen argumentum: " + a[0:])


for fname in files:
    file = open(fname, "r", encoding="utf-8") # note: without encoding, the text is garbage
    fsplit = fname.split('/')[-1]
    txt = file.read()
    file.close()

    f = open("currentinput.txt", "w")
    #note: now we extract the text from the file and work with it in the following operations, so it is more modular (and probably efficient??)
    #but we can file.read() all the way, let's see if it works better this way or that way
    #UPDATE: we must create a file as well for docker

    f.write(txt)
    f.close()

    print("Elemzendo szoveg: \n", txt, '\n\n')

    if(is_emagyar):
        print("e-magyar elemzese indul\n.................................................................................................\n")
        e_tokens, e_lems, e_morph, e_ners, e_only_ners, e_pos, e_dep, e_head = emagyar(txt, fsplit, oute, e_tokens, e_lems, e_morph, e_ners, e_only_ners, e_pos, e_dep, e_head)
        print("\n\n\n")

    if(is_huspacy):
        print("huspacy elemzese indul\n.................................................................................................\n")
        h_tokens, h_lems, h_lems_em, h_udmorph, h_emm, h_ners, h_only_ners, h_pos, h_tag, h_udpos, h_dep, h_head = huspacy(txt, fsplit, outh, h_tokens, h_lems, h_lems_em, h_udmorph, h_emm, h_ners, h_only_ners, h_pos, h_tag, h_udpos, h_dep, h_head)
        print("\n\n\n")

print("Analysis over")

if(is_emagyar == True and is_huspacy == True):
    if(tok_comp):
        token_comparator(h_tokens, e_tokens)
        print('\n\n')
    if(morph_comp):
        morph_comparator(h_udmorph, h_emm, e_morph, h_tokens, e_tokens)
        print('\n\n')
    if(lem_comp):
        lemma_comparator(h_lems, h_lems_em, e_lems, h_tokens, e_tokens)
    if(ner_comp):
        ner_comparator(h_ners, h_only_ners, e_ners, e_only_ners, h_tokens, e_tokens)
    if(pos_comp):
        pos_comparator(h_pos, h_tag, h_udpos, e_pos, h_tokens, e_tokens)
    if(dep_comp):
        dep_comparator(h_dep, h_head, e_dep, e_head, h_tokens, e_tokens)

