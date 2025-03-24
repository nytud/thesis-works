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

    def print_to_csv(self, comp_data, fname_to_be):
        with open(f"eredmenyek/csv/{fname_to_be}_tok.csv", "a") as f:
            for s in self.comp_data[1]:
                f.write(s + "\n")
            
            


