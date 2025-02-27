from Comparator import Comparator
from packages.dep_converter import convert

class Dep_comparator(Comparator):
    def __init__(self, huspacy, emagyar):
        self.huspacy = huspacy
        self.emagyar = emagyar


    def str_to_print(self, j, k):
        return str(convert(self.huspacy.dep[j][1]) == self.emagyar.dep[k][1]) + "\t" +  str(str(self.huspacy.head[j][1]) == str(self.emagyar.head[k][1])) + '\t' + '|(' + self.huspacy.dep[j][1] + ')|' + "\t" + '|' + convert(self.huspacy.dep[j][1]) + '|' + '\t' + '|' + str(self.huspacy.head[j][1]) + '|' + '\t' + '|' + self.emagyar.dep[k][1] + '|' + '\t' + '|' + self.emagyar.head[k][1] + '|' + "\t\t" + "(" + self.huspacy.dep[j][0] + " " + self.huspacy.head[j][0] + " " + self.emagyar.dep[k][0] + " " + self.emagyar.head[k][0] + ")"

    def diff_to_print_e(self, k):
        return '\t\t|' + "_dep_" + '|' + '\t\t|' + "_head_" + '|' + "\t\t" + "(" + "_tok_" + ")"

    def diff_to_print_h(self, j):
        return '\t|' + "_dep_" + '|' + "\t" + "converted as: " + "_depconv_" + "\t" + '|' + "_head_" + '|' + "\t\t\t" + "(" + "_tok_" + ")"

    def compare(self):
        super().compare(self.huspacy, self.emagyar, "huspacy dep (original) \t huspacy huspacy dep (converted) \t huspacy head \t emagyar dep \t emagyar head")