from Comparator import Comparator

class Pos_comparator(Comparator):
    def __init__(self, huspacy, emagyar):
        self.huspacy = huspacy
        self.emagyar = emagyar


    def str_to_print(self, j, k):
        return str(self.huspacy.pos[j] == self.emagyar.pos[k] == self.huspacy.tag[j] == self.huspacy.pos_ud[j]) + '\t' + '|' + self.huspacy.pos[j] + '|' + '\t' + '|' + self.huspacy.tag[j] + '|' + '\t' + '|' + str(self.huspacy.pos_ud[j]) + '|' + '\t' + '|' + self.emagyar.pos[k] + '|' + "\t\t" + "(" + self.huspacy.tok[j] + " " + self.huspacy.tok[j] + " " + self.huspacy.tok[j] + " " + self.emagyar.tok[k] + ")"

    def diff_to_print_e(self, k):
        return '\t|' + '_pos_' + '|'+ "\t\t" + "(" + "_tok_" + ")"

    def diff_to_print_h(self, j):
        return '|' + '_pos_' + '|' + '\t' + '|' + '_tag_' + '|' + "\t" + '|' + '_posud_' + '|' + "\t\t" + "(" + "_tok_" + ")"

    def compare(self):
        super().compare(self.huspacy, self.emagyar, "huspacy pos \t huspacy tag \t huspacy (emmorph) ud pos \t emagyar pos")