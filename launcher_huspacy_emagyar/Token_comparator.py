from Comparator import Comparator

class Token_comparator(Comparator):
    def __init__(self, huspacy, emagyar):
        self.huspacy = huspacy
        self.emagyar = emagyar


    def str_to_print(self, j, k):
        return str(self.huspacy.tok[j][0] == self.emagyar.tok[k][0]) + '\t' + '|' + self.huspacy.tok[j][1] + '|' + '\t' + '|' + self.emagyar.tok[k][1] + '|'

    def diff_to_print_e(self, k):
        return '\t|' + self.emagyar.tok[k][1] + '|'

    def diff_to_print_h(self, j):
        return '|' + self.huspacy.tok[j][1] + '|'

    def compare(self):
        super().compare(self.huspacy, self.emagyar, "huspacy tokenek \t emagyar tokenek")

