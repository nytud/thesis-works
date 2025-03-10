from Comparator import Comparator
from packages.dep_converter import convert

class Dep_comparator(Comparator):
    def __init__(self, huspacy, emagyar):
        self.huspacy = huspacy
        self.emagyar = emagyar


    def str_to_print(self, j, k):
        return str(convert(self.huspacy.dep[j]) == self.emagyar.dep[k]) + "\t" +  str(str(self.huspacy.head[j]) == str(self.emagyar.head[k])) + '\t' + '|(' + self.huspacy.dep[j] + ')|' + "\t" + '|' + convert(self.huspacy.dep[j]) + '|' + '\t' + '|' + str(self.huspacy.head[j]) + '|' + '\t' + '|' + self.emagyar.dep[k] + '|' + '\t' + '|' + self.emagyar.head[k] + '|' + "\t\t" + "(" + self.huspacy.tok[j] + " " + self.huspacy.tok[j] + " " + self.emagyar.tok[k] + " " + self.emagyar.tok[k] + ")"

    def diff_to_print_e(self, k):
        return '\t\t|' + "_dep_" + '|' + '\t\t|' + "_head_" + '|' + "\t\t" + "(" + "_tok_" + ")"

    def diff_to_print_h(self, j):
        return '\t|' + "_dep_" + '|' + "\t" + "converted as: " + "_depconv_" + "\t" + '|' + "_head_" + '|' + "\t\t\t" + "(" + "_tok_" + ")"

    def compare(self):
        super().compare(self.huspacy, self.emagyar, "huspacy dep (original) \t huspacy huspacy dep (converted) \t huspacy head \t emagyar dep \t emagyar head")