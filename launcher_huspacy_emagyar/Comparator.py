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




    """def token_comparator(h_tokens, e_tokens):
        l = min(len(h_tokens), len(e_tokens))
        print("huspacy tokenszám: ", len(h_tokens))
        print("e-magyar tokenszám: ", len(e_tokens))

        j = 0
        k = 0
        print("huspacy tokenek \t emagyar tokenek")

        
        while(j != len(h_tokens) and k != len(e_tokens)):
            #normal case: synchronous tokenization
            if(h_tokens[j] == e_tokens[k]):
                print(str_to_print(j, k, h_tokens, e_tokens, None, None, None, None, None))
                print("_______________________________________________________")
                j = j + 1
                k = k + 1
            #abnormal case: tokenization glitch - diffsolving required
            else:
                m = False #modified
                for z in range(1,6):
                    if(m):
                        break
                    for v in range(1,6):
                        j, k, m = diffsolver(z, v, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, None, None, None, None, None)
                        if(m):
                            break
                        j, k, m = diffsolver(v, z, j, k, h_tokens, e_tokens, str_to_print, diff_to_print_e, diff_to_print_h, None, None, None, None, None)
                        if(m):
                            break
                if(m):
                    continue


                
                
            
                print(str_to_print(j, k, h_tokens, e_tokens, None, None, None, None, None))
                print("_______________________________________________________")
                j = j + 1
                k = k + 1
        
                break

        #print the remains
        if(j != len(h_tokens)):
            print("huspacy maradek token: ")
            print(h_tokens[j:])
            
        if(k != len(e_tokens)):
            print("emagyar maradek token: ")
            print(e_tokens[k:])"""


