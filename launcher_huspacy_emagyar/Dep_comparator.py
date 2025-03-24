from Comparator import Comparator
from packages.dep_converter import convert

class Dep_comparator(Comparator):
    def __init__(self, huspacy, emagyar):
        self.huspacy = huspacy
        self.emagyar = emagyar


    def str_to_print(self, j, k):
        return f"{convert(self.huspacy.dep[j]) == self.emagyar.dep[k]}\t{str(self.huspacy.head[j]) == str(self.emagyar.head[k])}\t|({self.huspacy.dep[j]})|\t|{convert(self.huspacy.dep[j])}|\t|{self.huspacy.head[j]}|\t|{self.emagyar.dep[k]}|\t|{self.emagyar.head[k]}|\t\t({self.huspacy.tok[j]} {self.huspacy.tok[j]} {self.emagyar.tok[k]} {self.emagyar.tok[k]})"

    def diff_to_print_e(self, k):
        return f"\t\t|_dep_|\t\t|_head_|\t\t(_tok_)"

    def diff_to_print_h(self, j):
        return f"\t|_dep_|\tconverted as: _depconv_\t|_head_|\t\t\t(_tok_)"

    def csv_to_print(self, j, k):
        pass

    def csv_diff_to_print_e(self, k):
        pass

    def csv_diff_to_print_h(self, j):
        pass

    def compare(self):
        super().compare(self.huspacy, self.emagyar, "huspacy dep (original) \t huspacy huspacy dep (converted) \t huspacy head \t emagyar dep \t emagyar head")