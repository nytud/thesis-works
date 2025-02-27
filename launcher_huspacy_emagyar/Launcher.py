import glob

from Huspacy import Huspacy
from Emagyar import Emagyar
from Token_comparator import Token_comparator
from Morph_comparator import Morph_comparator
from Lemma_comparator import Lemma_comparator
from Pos_comparator import Pos_comparator

class Launcher:
    def __init__(self, args):
        self.args = args

        self.oute = False
        self.outh = False
        self.is_emagyar = False
        self.is_huspacy = False
        self.tok_comp = False
        self.morph_comp = False
        self.lem_comp = False
        self.ner_comp = False
        self.pos_comp = False
        self.dep_comp = False

        if("-emagyar" in list(args)):
            self.is_emagyar = True

        if("-huspacy" in list(args)):
            self.is_huspacy = True

        if("-oute" in list(args)):
            self.oute = True

        if("-outh" in list(args)):
            self.outh = True

        if("-tok" in list(args)):
            self.tok_comp = True

        if("-morph" in list(args)):
            self.morph_comp = True

        if("-lem" in list(args)):
            self.lem_comp = True

        if("-ner" in list(args)):
            self.ner_comp = True

        if("-pos" in list(args)):
            self.pos_comp = True

        if("-dep" in list(args)):
            self.dep_comp = True


        self.files = list([])

        for a in args:
            if(a[-4:] == ".txt"):
                self.files = self.files + glob.glob(a)
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

        self.huspacy = Huspacy()
        self.emagyar = Emagyar()


    def launch_huspacy(self):
        for fname in self.files:
            txt = ""
            fsplit = ""
            with open(fname, "r", encoding="utf-8") as file: # note: without encoding, the text is garbage
                fsplit = fname.split('/')[-1]
                txt = file.read()

            with open("currentinput.txt", "w") as f:
                f.write(txt)

            print("Elemzendo szoveg: \n", txt, '\n\n')

            self.huspacy.run(fsplit, txt)

            if(self.outh):
                self.huspacy.print(fsplit)

    def launch_emagyar(self):
        for fname in self.files:
            txt = ""
            fsplit = ""
            with open(fname, "r", encoding="utf-8") as file: # note: without encoding, the text is garbage
                fsplit = fname.split('/')[-1]
                txt = file.read()

            with open("currentinput.txt", "w") as f:
                f.write(txt)

            #print("Elemzendo szoveg: \n", txt, '\n\n')

            self.emagyar.run(fsplit, txt)

            if(self.oute):
                self.emagyar.print(fsplit)

            

    def compare_tokens(self):
        if(self.tok_comp):
            token_comparator = Token_comparator(self.huspacy, self.emagyar)
            #print(token_comparator.str_to_print(0,0))
            #print(token_comparator.diff_to_print_e(0))
            #print(token_comparator.diff_to_print_h(0))
            token_comparator.compare()

    def compare_morph(self):
        if(self.morph_comp):
            morph_comparator = Morph_comparator(self.huspacy, self.emagyar)
            morph_comparator.compare()

    def compare_lemma(self):
        if(self.lem_comp):
            lemma_comparator = Lemma_comparator(self.huspacy, self.emagyar)
            lemma_comparator.compare()

    def compare_pos(self):
        if(self.pos_comp):
            pos_comparator = Pos_comparator(self.huspacy, self.emagyar)
            pos_comparator.compare()

    def compare_dep(self):
        pass

    def compare_ner(self):
        pass


        
