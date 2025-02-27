from Comparator import Comparator

class Ner_comparator(Comparator):
    def __init__(self, huspacy, emagyar):
        self.huspacy = huspacy
        self.emagyar = emagyar


    def str_to_print(self, j, k):
        return str(self.huspacy.ner[j][1] == self.emagyar.ner[k][1]) + '\t' +  '|' + self.huspacy.ner[j][1] + '|' + '\t' + '|' + self.emagyar.ner[k][1] + '|' + "\t\t" + "(" + self.huspacy.ner[j][0] + " " + self.emagyar.ner[k][0] + ")"

    def diff_to_print_e(self, k):
        return '\t\t|' + "_ner_" + '|'+ "\t\t" + "(" + "_tok_" + ")"

    def diff_to_print_h(self, j):
        return '|' + "_ner_" + '|'+ "\t\t\t" + "(" + "_tok_" + ")"

    def compare(self):
        super().compare(self.huspacy, self.emagyar, "huspacy ner \t emagyar ner")