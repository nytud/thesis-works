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
        comp_data = [[],[],[],[]]

        l = min(len(huspacy.tok), len(emagyar.tok))
        comp_data[0].append(f"HuSpaCy tokenszám: {len(huspacy.tok)}")
        comp_data[0].append(f"e-magyar tokenszám: {len(emagyar.tok)}")
        
        comp_data[0].append(headline)
        comp_data[1].append(headline)

        j = 0
        k = 0
        #print(headline)

        diffsolver = Diffsolver(self.huspacy, self.emagyar)
        while(j != len(huspacy.tok) and k != len(emagyar.tok)):
            #normal case: synchronous tokenization
            if(huspacy.tok[j] == emagyar.tok[k]):
                comp_data[0].append(self.str_to_print(j,k))
                comp_data[1].append(self.csv_to_print(j,k))
            
                
                j = j + 1
                k = k + 1
                #abnormal case: tokenization glitch - diffsolving required
            else:
                #append the false, differing tokens
                comp_data[0].append(self.str_to_print(j,k))
                comp_data[1].append(self.csv_to_print(j,k))
                #must step one because we want to handle the remains AFTER the differing ones
                j = j + 1
                k = k + 1

                m = False #modified
                for z in range(0,6):
                    if(m):
                        break #from z-for; because right z and v just have been found in the previous z-iteration

                    for v in range(0,6):
                        j, k, m, comp_data = diffsolver.solve(self.diff_to_print_e(k), self.diff_to_print_h(j), self.csv_diff_to_print_e(k), self.csv_diff_to_print_h(j), z, v, j, k, comp_data)
                        
                        if(m):
                            break #from v-for; because rigth z and v just have been found in the previous v-iteration
                        
                        j, k, m, comp_data = diffsolver.solve(self.diff_to_print_e(k), self.diff_to_print_h(j), self.csv_diff_to_print_e(k), self.csv_diff_to_print_h(j), v, z, j, k, comp_data)
                        
                        if(m):
                            break #from v-for; because rigth z and v just have been found in the previous v-iteration

                        #NOTE: solve has to be called twice to ensure it finds the optimal shifts
                if(m):
                    #move on to the next j and k in while
                    continue


                if(j != len(huspacy.tok) and k != len(emagyar.tok)):
                    comp_data[0].append(self.str_to_print(j,k))
                    comp_data[1].append(self.csv_to_print(j,k))
                    
                j = j + 1
                k = k + 1

                break

        #print the remains
        if(j != len(huspacy.tok)):
            comp_data[0].append("huspacy maradek token: ")
            comp_data[0] += huspacy.tok[j:]
            
        if(k != len(emagyar.tok)):
            comp_data[0].append("emagyar maradek token: ")
            comp_data[0] += emagyar.tok[k:]


        return comp_data


