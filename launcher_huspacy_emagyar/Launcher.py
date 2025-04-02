import glob
import os
import sys

from Huspacy import Huspacy
from Emagyar import Emagyar
from Token_comparator import Token_comparator
from Morph_comparator import Morph_comparator
from Lemma_comparator import Lemma_comparator
from Pos_comparator import Pos_comparator
from Dep_comparator import Dep_comparator
from Ner_comparator import Ner_comparator
from Printer import Printer


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
        self.csv = False
    

        self.tok_res = []
        self.morph_res = []
        self.lem_res = []
        self.pos_res = []
        self.dep_res = []
        self.ner_res = []

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

        if("-csv" in list(args)):
            self.csv = True
        


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
                or a == "-dep"
                or a == "-csv"):
                pass
            else:
                sys.exit("Hiba: ismeretlen argumentum: " + a[0:])

        self.huspacy = Huspacy()
        self.emagyar = Emagyar()


    
    def launch(self):
        for fname in self.files:
            txt = ""
            fname_to_be = ""

            with open(fname, "r", encoding="utf-8") as file:
                fname_to_be = fname.split('/')[-1]
                txt = file.read()

            #print(f"Elemzendo szoveg: \n {txt}\n\n")

            try:
                os.mkdir("eredmenyek")
            except FileExistsError:
                pass
            except Exception as e:
                #print(f"Hiba a mappa létrehozásakor: {e}\nSegítség: próbálja meg manuálisan létrehozni megfelelő jogosultsággal!")
                sys.exit()

            try:
                os.makedirs("eredmenyek/huspacy")
            except FileExistsError:
                pass
            except Exception as e:
                #print(f"Hiba a mappa létrehozásakor: {e}\nSegítség: próbálja meg manuálisan létrehozni megfelelő jogosultsággal!")
                sys.exit()

            try:
                os.makedirs("eredmenyek/emagyar")
            except FileExistsError:
                pass
            except Exception as e:
                #print(f"Hiba a mappa létrehozásakor: {e}\nSegítség: próbálja meg manuálisan létrehozni megfelelő jogosultsággal!")
                sys.exit()

            try:
                if(self.is_emagyar):
                    #print("e-magyar indul")
                    #(coldb, rowdb) = os.get_terminal_size()
                    #for i in range(coldb):
                        #print(".", end="")
                    #print("\n")
                    self.emagyar.run(fname_to_be, txt)

                    if(self.oute):
                        pass
                        #self.emagyar.print(fname_to_be)
                
                if(self.is_huspacy):
                    #print("huspacy indul")
                    #(coldb, rowdb) = os.get_terminal_size()
                    #for i in range(coldb):
                    #    print(".", end="")
                    #print("\n")
                    self.huspacy.run(fname_to_be, txt)

                    if(self.outh):
                        pass
                        #self.huspacy.print(fname_to_be)


                fname_short = fname_to_be[:-4]

                self.compare_tokens(fname_short)
                self.compare_morph(fname_short)
                self.compare_lemma(fname_short)
                self.compare_pos(fname_short)
                self.compare_dep(fname_short)
                self.compare_ner(fname_short)
            except Exception as e:
                raise Exception(e)
                #print("ERROR:")
                #print(e)    
            

    def compare_tokens(self, fname_short):
        if(self.tok_comp):
            token_comparator = Token_comparator(self.huspacy, self.emagyar)
            comp_data = token_comparator.compare()

            printer = Printer(comp_data)
            self.tok_res = printer.print_normal()


            if(self.csv):
                try:
                    os.makedirs("eredmenyek/csv")
                except FileExistsError:
                    pass
                except Exception as e:
                    #print(f"Hiba a mappa létrehozásakor: {e} \nSegítség: próbálja meg manuálisan létrehozni megfelelő jogosultsággal!")
                    sys.exit()
            
                with open(f"eredmenyek/csv/{fname_short}_tok.csv", "w") as csvfile:
                    pass                                                        #creating empty file
            
                printer.print_to_csv(comp_data, fname_short, "tok")

            


    def compare_morph(self, fname_short):
        if(self.morph_comp):
            morph_comparator = Morph_comparator(self.huspacy, self.emagyar)
            comp_data = morph_comparator.compare()

            printer = Printer(comp_data)
            self.morph_res = printer.print_normal()


            if(self.csv):
                try:
                    os.makedirs("eredmenyek/csv")
                except FileExistsError:
                    pass
                except Exception as e:
                    #print(f"Hiba a mappa létrehozásakor: {e} \nSegítség: próbálja meg manuálisan létrehozni megfelelő jogosultsággal!")
                    sys.exit()
            
                with open(f"eredmenyek/csv/{fname_short}_morph.csv", "w") as csvfile:
                    pass                                                        #creating empty file
            
                printer.print_to_csv(comp_data, fname_short, "morph")



    def compare_lemma(self, fname_short):
        if(self.lem_comp):
            lemma_comparator = Lemma_comparator(self.huspacy, self.emagyar)
            comp_data = lemma_comparator.compare()

            printer = Printer(comp_data)
            #printer.print_normal()


            if(self.csv):
                try:
                    os.makedirs("eredmenyek/csv")
                except FileExistsError:
                    pass
                except Exception as e:
                    #print(f"Hiba a mappa létrehozásakor: {e} \nSegítség: próbálja meg manuálisan létrehozni megfelelő jogosultsággal!")
                    sys.exit()
            
                with open(f"eredmenyek/csv/{fname_short}_lem.csv", "w") as csvfile:
                    pass                                                        #creating empty file
            
                printer.print_to_csv(comp_data, fname_short, "lem")


    def compare_pos(self, fname_short):
        if(self.pos_comp):
            pos_comparator = Pos_comparator(self.huspacy, self.emagyar)
            comp_data = pos_comparator.compare()

            printer = Printer(comp_data)
            #printer.print_normal()


            if(self.csv):
                try:
                    os.makedirs("eredmenyek/csv")
                except FileExistsError:
                    pass
                except Exception as e:
                    #print(f"Hiba a mappa létrehozásakor: {e} \nSegítség: próbálja meg manuálisan létrehozni megfelelő jogosultsággal!")
                    sys.exit()
            
                with open(f"eredmenyek/csv/{fname_short}_pos.csv", "w") as csvfile:
                    pass                                                        #creating empty file
            
                printer.print_to_csv(comp_data, fname_short, "pos")



    def compare_dep(self, fname_short):
        if(self.dep_comp):
            dep_comparator = Dep_comparator(self.huspacy, self.emagyar)
            comp_data = dep_comparator.compare()

            printer = Printer(comp_data)
            #printer.print_normal()


            if(self.csv):
                try:
                    os.makedirs("eredmenyek/csv")
                except FileExistsError:
                    pass
                except Exception as e:
                    #print(f"Hiba a mappa létrehozásakor: {e} \nSegítség: próbálja meg manuálisan létrehozni megfelelő jogosultsággal!")
                    sys.exit()
            
                with open(f"eredmenyek/csv/{fname_short}_dep.csv", "w") as csvfile:
                    pass                                                        #creating empty file
            
                printer.print_to_csv(comp_data, fname_short, "dep")


    def compare_ner(self, fname_short):
        if(self.ner_comp):
            ner_comparator = Ner_comparator(self.huspacy, self.emagyar)
            comp_data = ner_comparator.compare()

            printer = Printer(comp_data)
            #printer.print_normal()


            if(self.csv):
                try:
                    os.makedirs("eredmenyek/csv")
                except FileExistsError:
                    pass
                except Exception as e:
                    #print(f"Hiba a mappa létrehozásakor: {e} \nSegítség: próbálja meg manuálisan létrehozni megfelelő jogosultsággal!")
                    sys.exit()
            
                with open(f"eredmenyek/csv/{fname_short}_ner.csv", "w") as csvfile:
                    pass                                                        #creating empty file

                with open(f"eredmenyek/csv/{fname_short}_onlyner.csv", "w") as csvfile:
                    pass                                                        #creating empty file
            
                printer.print_to_csv(comp_data, fname_short, "ner")







        
