import sys
import glob

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


    def launch_huspacy():
        pass

    def launch_emagyar():
        pass

    def compare_tokens():
        pass

    def compare_morph():
        pass

    def compare_lemma():
        pass

    def compare_pos():
        pass

    def compare_dep():
        pass

    def compare_ner():
        pass


        
