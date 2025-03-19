from Diffsolver import Diffsolver

from abcmeta import ABC
from abcmeta import abstractmethod
import os

class Comparator(ABC):

    #what to print with synchronous tokens
    @abstractmethod
    def str_to_print(self, j, k):
        pass

    #print emagyar remains in case of tokenization glitch when huspacy is ahead
    @abstractmethod
    def diff_to_print_e(self, k):
        pass

    #print huspacy remains in case of tokenization glitch when emagyar is ahead
    @abstractmethod
    def diff_to_print_h(self, j):
        pass

    @abstractmethod
    def csv_to_print(self, j, k):
        pass

    @abstractmethod
    def csv_diff_to_print_e(self, k):
        pass

    @abstractmethod
    def csv_diff_to_print_h(self, j):
        pass



    def compare(self, huspacy, emagyar, headline):
        l = min(len(huspacy.tok), len(emagyar.tok))
        print("huspacy tokenszám: ", len(huspacy.tok))
        print("e-magyar tokenszám: ", len(emagyar.tok))

        j = 0
        k = 0
        print(headline)

        comp_data = [[],[]]

        
        while(j != len(huspacy.tok) and k != len(emagyar.tok)):
            #normal case: synchronous tokenization
            if(huspacy.tok[j][0] == emagyar.tok[k][0]):
                comp_data[0].append(self.str_to_print(j,k))
                comp_data[1].append(self.csv_to_print(j,k))
                ###print(self.str_to_print(j, k))
                ###(coldb, rowdb) = os.get_terminal_size()
                ###for i in range(coldb):
                    ###print("_", end="")
                ###print("\n")
                
                j = j + 1
                k = k + 1
                #abnormal case: tokenization glitch - diffsolving required
            else:
                m = False #modified
                for z in range(1,6):
                    if(m):
                        break
                    for v in range(1,6):
                        ###diffsolver = Diffsolver(self.huspacy, self.emagyar, z, v, j, k, self.str_to_print(j,k), self.diff_to_print_e(k), self.diff_to_print_h(j))
                        ###j, k, m = diffsolver.print()
                        diffsolver = Diffsolver(self.huspacy, self.emagyar, z, v, j, k, comp_data)
                        j, k, m, comp_data = diffsolver.solve(self.str_to_print(j,k), self.diff_to_print_e(k), self.diff_to_print_h(j), self.csv_to_print(j,k), self.csv_diff_to_print_e(k), self.csv_diff_to_print_h(j))
                        if(m):
                            break
                        ###diffsolver = Diffsolver(self.huspacy, self.emagyar, v, z, j, k, self.str_to_print(j,k), self.diff_to_print_e(k), self.diff_to_print_h(j))
                        ###j, k, m = diffsolver.print()
                        diffsolver = Diffsolver(self.huspacy, self.emagyar, v, z, j, k, comp_data)
                        j, k, m, comp_data = diffsolver.solve(self.str_to_print(j,k), self.diff_to_print_e(k), self.diff_to_print_h(j), self.csv_to_print(j,k), self.csv_diff_to_print_e(k), self.csv_diff_to_print_h(j))
                        if(m):
                            break
                if(m):
                    continue


                comp_data[0].append(self.str_to_print(j,k))
                comp_data[1].append(self.csv_to_print(j,k))
                ###print(self.str_to_print(j, k))
                ###(coldb, rowdb) = os.get_terminal_size()
                ###for i in range(coldb):
                    ###print("_", end="")
                ###print("\n")
                j = j + 1
                k = k + 1
        
                break

        #print the remains
        if(j != len(huspacy.tok)):
            print("huspacy maradek token: ")
            print(huspacy.tok[j:])
            
        if(k != len(emagyar.tok)):
            print("emagyar maradek token: ")
            print(emagyar.tok[k:])


        print(comp_data[0], sep="\n")
        #print(comp_data[1])


