from Huspacy import Huspacy
from Emagyar import Emagyar

class Diffsolver:
    def __init__(self, huspacy, emagyar, jj, kk, j, k, str_to_print, diff_to_print_e, diff_to_print_h):
        self.huspacy = huspacy
        self.emagyar = emagyar
        self.jj = jj
        self.kk = kk
        self.j = j
        self.k = k
        self.str_to_print = str_to_print
        self.diff_to_print_e = diff_to_print_e
        self.diff_to_print_h = diff_to_print_h

    def print(self):
        modified = False
        if(self.k+self.kk < len(self.emagyar.tok) and self.j+self.jj < len(self.huspacy.tok)): #prevent index error
            if(self.k != len(self.emagyar.tok)-self.kk and self.j != len(self.huspacy.tok)-self.jj and  self.huspacy.tok[self.j+self.jj] == self.emagyar.tok[self.k+self.kk]): #found the next match
                print(self.str_to_print) #we print it as usual, because it is a match
                print("_______________________________________________________")
                self.k = self.k + 1
                self.j = self.j + 1
                if(self.kk > self.jj): #emagyar shift was greater -> huspacy is ahead -> emagyar remains are to be printed
                    for i in range (0, self.kk-self.jj):
                        print("emagyar\t" + self.diff_to_print_e)
                        print("_______________________________________________________")
                        self.k = self.k+1
                else:
                    for i in range (0, self.jj-self.kk): #huspacy shift was greater -> emagyar is ahead -> huspacy remains are to be printed
                        print("huspacy\t" + self.diff_to_print_h)
                        print("_______________________________________________________")
                        self.j = self.j+1

                print(self.str_to_print) #have to resume teh printout as normal
                print("_______________________________________________________")
                self.j = self.j + 1
                self.k = self.k + 1
                modified = True #means: the diffsolving is done, the original print has been modified accordingly
                #False only when diffsolver was called with wrong shift combination

        return self.j, self.k, modified
