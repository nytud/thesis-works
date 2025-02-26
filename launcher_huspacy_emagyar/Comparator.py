from packages.diffsolver import diffsolver

from abcmeta import ABC
from abcmeta import abstractmethod

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



    def compare(self, huspacy, emagyar, headline):
        l = min(len(huspacy.tok), len(emagyar.tok))
        print("huspacy tokenszám: ", len(huspacy.tok))
        print("e-magyar tokenszám: ", len(emagyar.tok))

        j = 0
        k = 0
        print(headline)

        
        while(j != len(huspacy.tok) and k != len(emagyar.tok)):
            #normal case: synchronous tokenization
            if(huspacy.tok[j][0] == emagyar.tok[k][0]):
                print(self.str_to_print(j, k))
                print("_______________________________________________________")
                j = j + 1
                k = k + 1
                #abnormal case: tokenization glitch - diffsolving required
            else:
                """m = False #modified
                for z in range(1,6):
                    if(m):
                        break
                    for v in range(1,6):
                        #j, k, m = diffsolver(z, v, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, None, None, None, None, None)
                        if(m):
                            break
                        #j, k, m = diffsolver(v, z, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, None, None, None, None, None)
                        if(m):
                            break
                if(m):
                    continue"""


                
                
            
                print(self.str_to_print(j, k))
                print("_______________________________________________________")
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


