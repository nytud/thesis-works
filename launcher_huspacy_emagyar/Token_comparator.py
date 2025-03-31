from Comparator import Comparator

class Token_comparator(Comparator):
    def __init__(self, huspacy, emagyar):
        self.huspacy = huspacy
        self.emagyar = emagyar


    def str_to_print(self, j, k):
        return f"{self.huspacy.tok[j] == self.emagyar.tok[k]}\t|{self.huspacy.tok[j]}|\t|{self.emagyar.tok[k]}|"

    def diff_to_print_e(self, k):
        return f"\t|_tok_|"

    def diff_to_print_h(self, j):
        return f"|_tok_|"

    def csv_to_print(self, j, k):
        return f'"{self.huspacy.tok[j] == self.emagyar.tok[k]}","|{self.huspacy.tok[j]}|","|{self.emagyar.tok[k]}|"'

    def csv_diff_to_print_e(self, k):
        return f'"","","|_tok_|"'

    def csv_diff_to_print_h(self, j):
        return f'"","|_tok_|",""'

    def compare(self):
        return super().compare(self.huspacy, self.emagyar, "huspacy tokenek \t emagyar tokenek")

