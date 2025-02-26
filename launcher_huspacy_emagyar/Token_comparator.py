from Comparator import Comparator

class Token_comparator(Comparator):
    def __init__(self, huspacy, emagyar):
        self.huspacy = huspacy
        self.emagyar = emagyar


    def str_to_print(self, j, k):
        return str(self.huspacy.tok[j] == self.emagyar.tok[k]) + '\t' + '|' + self.huspacy.tok[j] + '|' + '\t' + '|' + self.emagyar.tok[k] + '|'

    def diff_to_print_e(self, k):
        return '\t|' + self.emagyar.tok[k] + '|'

    def diff_to_print_h(self, j):
        return '|' + self.huspacy.tok[j] + '|'

