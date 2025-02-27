from Comparator import Comparator

class Morph_comparator(Comparator):
    def __init__(self, huspacy, emagyar):
        self.huspacy = huspacy
        self.emagyar = emagyar


    def str_to_print(self, j, k):
        return str(self.huspacy.morph_em[j][1] == self.emagyar.morph[k][1]) + '\t' + '|' + self.huspacy.morph_ud[j][1]  + '|' + '\t' + '|' + self.huspacy.morph_em[j][1] + '|' + '\t' + '|' + self.emagyar.morph[k][1] + '|' + "\t\t" + "(" + self.huspacy.morph_ud[j][0] + " " + self.huspacy.morph_em[j][0] + " " + self.emagyar.morph[k][0] + ")"

    def diff_to_print_e(self, k):
        return '\t|' + '_morph_' + '|'+ "\t\t" + "(" + "_tok_" + ")"

    def diff_to_print_h(self, j):
        return '|' + '_morphud_' + '|' + '\t' + '|' + '_morphem_' + '|' + "\t\t\t" + "(" + "_tok_" + ")"

    def compare(self):
        super().compare(self.huspacy, self.emagyar, "huspacy ud \t huspacy emmorph \t emagyar morph")