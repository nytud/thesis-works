from Comparator import Comparator

class Lemma_comparator(Comparator):
    def __init__(self, huspacy, emagyar):
        self.huspacy = huspacy
        self.emagyar = emagyar


    def str_to_print(self, j, k):
        return str(self.huspacy.lem[j][1] == self.emagyar.lem[k][1] == self.huspacy.lem_em[j][1]) + '\t' + '|' + self.huspacy.lem[j][1] + '|' + '\t' + '|' + str(self.huspacy.lem_em[j][1]) + '|' + '\t' + '|' + self.emagyar.lem[k][1] + '|' + "\t\t" + "(" + self.huspacy.lem_em[j][0] + " " + self.huspacy.lem[j][0] + " " + self.emagyar.lem[k][0] + ")"

    def diff_to_print_e(self, k):
        return '\t|' + '_lem_' + '|'+ "\t\t" + "(" + "_tok_" + ")"

    def diff_to_print_h(self, j):
        return '|' + '_lem_' + '|' + '\t' + '|' + '_lemem_' + '|' + "\t\t\t" + "(" + "_tok_" + ")"

    def compare(self):
        super().compare(self.huspacy, self.emagyar, "huspacy lemma \t huspacy emmorph lemma \t emagyar lemma")