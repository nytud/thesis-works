import os

class Printer:
    def __init__(self, comp_data):
        self.comp_data = comp_data


    def print_normal(self):
        (coldb, rowdb) = os.get_terminal_size()

        for s in self.comp_data[0]:
            for i in range(coldb):
                print("_", end="")
            print("\n")
            print(s)
            


