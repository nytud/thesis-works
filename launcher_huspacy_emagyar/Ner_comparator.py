from Comparator import Comparator

from Only_Ner import Only_Ner

class Ner_comparator(Comparator):
    def __init__(self, huspacy, emagyar):
        self.huspacy = huspacy
        self.emagyar = emagyar


    def str_to_print(self, j, k):
        return str(self.huspacy.ner[j] == self.emagyar.ner[k]) + '\t' +  '|' + self.huspacy.ner[j] + '|' + '\t' + '|' + self.emagyar.ner[k] + '|' + "\t\t" + "(" + self.huspacy.tok[j] + " " + self.emagyar.tok[k] + ")"

    def diff_to_print_e(self, k):
        return '\t\t|' + "_ner_" + '|'+ "\t\t" + "(" + "_tok_" + ")"

    def diff_to_print_h(self, j):
        return '|' + "_ner_" + '|'+ "\t\t\t" + "(" + "_tok_" + ")"

    def compare(self):
        super().compare(self.huspacy, self.emagyar, "huspacy ner \t emagyar ner")
        only_ner = Only_Ner(self.huspacy, self.emagyar)
        only_ner.print()