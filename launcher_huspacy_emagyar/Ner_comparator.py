from Comparator import Comparator

from Only_Ner import Only_Ner

class Ner_comparator(Comparator):
    def __init__(self, huspacy, emagyar):
        self.huspacy = huspacy
        self.emagyar = emagyar


    def str_to_print(self, j, k):
        return f"{self.huspacy.ner[j] == self.emagyar.ner[k]}\t|{self.huspacy.ner[j]}|\t|{self.emagyar.ner[k]}|\t\t({self.huspacy.tok[j]} {self.emagyar.tok[k]})"

    def diff_to_print_e(self, k):
        return f"\t\t|_ner_|\t\t(_tok_)"

    def diff_to_print_h(self, j):
        return f"|_ner_|\t\t\t(_tok_)"

    def csv_to_print(self, j, k):
        pass

    def csv_diff_to_print_e(self, k):
        pass

    def csv_diff_to_print_h(self, j):
        pass

    def compare(self):
        super().compare(self.huspacy, self.emagyar, "huspacy ner \t emagyar ner")
        only_ner = Only_Ner(self.huspacy, self.emagyar)
        only_ner.print()