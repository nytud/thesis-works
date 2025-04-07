from Comparator import Comparator

class Morph_comparator(Comparator):
    def __init__(self, huspacy, emagyar):
        self.huspacy = huspacy
        self.emagyar = emagyar


    def str_to_print(self, j, k):
        return f"{self.huspacy.morph_em[j] == self.emagyar.morph[k]}\t|{self.huspacy.morph_ud[j]}|\t|{self.huspacy.morph_em[j]}|\t|{self.emagyar.morph[k]}|\t\t({self.huspacy.tok[j]} {self.emagyar.tok[k]})"

    def diff_to_print_e(self, k):
        return f"\t|_morph_|\t\t(_tok_)"

    def diff_to_print_h(self, j):
        return f"|_morphud_|\t|_morphem_|\t\t\t(_tok_)"

    def csv_to_print(self, j, k):
        return f'"{self.huspacy.morph_em[j] == self.emagyar.morph[k]}","|{self.huspacy.morph_ud[j]}|","|{self.huspacy.morph_em[j]}|","|{self.emagyar.morph[k]}|","|{self.huspacy.tok[j]}|","|{self.emagyar.tok[k]}|"'

    def csv_diff_to_print_e(self, k):
        return f'"","","","|_morph_|","","|_tok_|"'

    def csv_diff_to_print_h(self, j):
        return f'"","|_morphud_|","|_morphem_|","|_tok_|"'

    def compare(self):
        return super().compare(self.huspacy, self.emagyar, "összehasonlítás \t huspacy ud \t huspacy emmorph \t emagyar morph")