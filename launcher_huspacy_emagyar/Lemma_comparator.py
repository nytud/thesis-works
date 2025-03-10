from Comparator import Comparator

class Lemma_comparator(Comparator):
    def __init__(self, huspacy, emagyar):
        self.huspacy = huspacy
        self.emagyar = emagyar


    def str_to_print(self, j, k):
        return str(self.huspacy.lem[j] == self.emagyar.lem[k] == self.huspacy.lem_em[j]) + '\t' + '|' + self.huspacy.lem[j] + '|' + '\t' + '|' + str(self.huspacy.lem_em[j]) + '|' + '\t' + '|' + self.emagyar.lem[k] + '|' + "\t\t" + "(" + self.huspacy.tok[j] + " " + self.huspacy.tok[j] + " " + self.emagyar.tok[k] + ")"

    def diff_to_print_e(self, k):
        return '\t|' + '_lem_' + '|'+ "\t\t" + "(" + "_tok_" + ")"

    def diff_to_print_h(self, j):
        return '|' + '_lem_' + '|' + '\t' + '|' + '_lemem_' + '|' + "\t\t\t" + "(" + "_tok_" + ")"

    def compare(self):
        super().compare(self.huspacy, self.emagyar, "huspacy lemma \t huspacy emmorph lemma \t emagyar lemma")