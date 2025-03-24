from Comparator import Comparator

class Lemma_comparator(Comparator):
    def __init__(self, huspacy, emagyar):
        self.huspacy = huspacy
        self.emagyar = emagyar


    def str_to_print(self, j, k):
        return f"{self.huspacy.lem[j] == self.emagyar.lem[k] == self.huspacy.lem_em[j]}\t|{self.huspacy.lem[j]}|\t|{self.huspacy.lem_em[j]}|\t|{self.emagyar.lem[k]}|\t\t({self.huspacy.tok[j]} {self.huspacy.tok[j]} {self.emagyar.tok[k]})"

    def diff_to_print_e(self, k):
        return f"\t|_lem_|\t\t(_tok_)"

    def diff_to_print_h(self, j):
        return f"|_lem_|\t|_lemem_|\t\t\t(_tok_)"

    def csv_to_print(self, j, k):
        pass

    def csv_diff_to_print_e(self, k):
        pass

    def csv_diff_to_print_h(self, j):
        pass

    def compare(self):
        super().compare(self.huspacy, self.emagyar, "huspacy lemma \t huspacy emmorph lemma \t emagyar lemma")