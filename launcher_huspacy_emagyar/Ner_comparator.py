from Comparator import Comparator

from Only_Ner import Only_Ner

class Ner_comparator(Comparator):
    def __init__(self, huspacy, emagyar):
        self.huspacy = huspacy
        self.emagyar = emagyar


    def str_to_print(self, j, k):
        return f"{self.huspacy.ner[j] == self.emagyar.ner[k]}\t|{self.huspacy.ner[j]}|\t|{self.emagyar.ner[k]}|\t({self.huspacy.tok[j]} {self.emagyar.tok[k]})"

    def diff_to_print_e(self, k):
        return f"\t\t|_ner_|\t\t(_tok_)"

    def diff_to_print_h(self, j):
        return f"|_ner_|\t\t\t(_tok_)"

    def csv_to_print(self, j, k):
        return f'"{self.huspacy.ner[j] == self.emagyar.ner[k]}","|{self.huspacy.ner[j]}|""|{self.emagyar.ner[k]}|","|{self.huspacy.tok[j]}|","|{self.emagyar.tok[k]}|"'

    def csv_diff_to_print_e(self, k):
        return f'"","","|_ner_|","","|_tok_|"'

    def csv_diff_to_print_h(self, j):
        return f'"","|_ner_|","","","|_tok_|"'

    def compare(self):
        comp_data = super().compare(self.huspacy, self.emagyar, "összehasonlítás\tHuSpaCy IOB\te-magyar IOB")
        only_ner = Only_Ner(self.huspacy, self.emagyar)
        only_ner.to_print(comp_data)
        return comp_data