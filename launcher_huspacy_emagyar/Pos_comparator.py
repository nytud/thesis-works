from Comparator import Comparator

class Pos_comparator(Comparator):
    def __init__(self, huspacy, emagyar):
        self.huspacy = huspacy
        self.emagyar = emagyar


    def str_to_print(self, j, k):
        return str(self.huspacy.pos[j][1] == self.emagyar.pos[k][1] == self.huspacy.tag[j][1] == self.huspacy.pos_ud[j][1]) + '\t' + '|' + self.huspacy.pos[j][1] + '|' + '\t' + '|' + self.huspacy.tag[j][1] + '|' + '\t' + '|' + str(self.huspacy.pos_ud[j][1]) + '|' + '\t' + '|' + self.emagyar.pos[k][1] + '|' + "\t\t" + "(" + self.huspacy.pos[j][0] + " " + self.huspacy.tag[j][0] + " " + self.huspacy.pos_ud[j][0] + " " + self.emagyar.pos[k][0] + ")"

    def diff_to_print_e(self, k):
        return '\t|' + '_pos_' + '|'+ "\t\t" + "(" + "_tok_" + ")"

    def diff_to_print_h(self, j):
        return '|' + '_pos_' + '|' + '\t' + '|' + '_tag_' + '|' + "\t" + '|' + '_posud_' + '|' + "\t\t" + "(" + "_tok_" + ")"

    def compare(self):
        super().compare(self.huspacy, self.emagyar, "huspacy pos \t huspacy tag \t huspacy (emmorph) ud pos \t emagyar pos")