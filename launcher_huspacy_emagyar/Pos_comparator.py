from Comparator import Comparator

class Pos_comparator(Comparator):
    def __init__(self, huspacy, emagyar):
        self.huspacy = huspacy
        self.emagyar = emagyar


    def str_to_print(self, j, k):
        return f"{self.huspacy.pos[j] == self.emagyar.pos[k] == self.huspacy.tag[j] == self.huspacy.pos_ud[j]}\t|{self.huspacy.pos[j]}|\t|{self.huspacy.tag[j]}|\t|{self.huspacy.pos_ud[j]}|\t|{self.emagyar.pos[k]}|\t({self.huspacy.tok[j]} {self.emagyar.tok[k]})"

    def diff_to_print_e(self, k):
        return f"\t|_pos_|\t\t(_tok_)"

    def diff_to_print_h(self, j):
        return f"|_pos_|\t|_tag_|\t|_posud_|\t\t(_tok_)"

    def csv_to_print(self, j, k):
        return f'"{self.huspacy.pos[j] == self.emagyar.pos[k] == self.huspacy.tag[j] == self.huspacy.pos_ud[j]}","|{self.huspacy.pos[j]}|","|{self.huspacy.tag[j]}|","|{self.huspacy.pos_ud[j]}|","|{self.emagyar.pos[k]}|","|{self.huspacy.tok[j]}|","|{self.emagyar.tok[k]}|"'

    def csv_diff_to_print_e(self, k):
        return f'"","|_pos_|","",|_tok_|"'

    def csv_diff_to_print_h(self, j):
        return f'"","|_pos_|","|_tag_|","|_posud_|","","|_tok_|"'

    def compare(self):
        return super().compare(self.huspacy, self.emagyar, "összehasonlítás\tHuSpaCy pos\tHuSpaCy tag\tHuSpaCy EmMorph UD POS\te-magyar POS")