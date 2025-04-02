import os

class Printer:
    def __init__(self, comp_data):
        self.comp_data = comp_data


    def print_normal(self):
        """(coldb, rowdb) = os.get_terminal_size()

        #metadata: fix indexes (0, 1, and 2)
        print(self.comp_data[0][0])
        print(self.comp_data[0][1])
        for i in range(coldb):
                print("-", end="")
        #header
        print(self.comp_data[0][2])

        for s in self.comp_data[0][3:]:
            for i in range(coldb):
                print("_", end="")
            print("\n")
            print(s)

        if len(self.comp_data[2]) > 0:
            for s in self.comp_data[2]:
                for i in range(coldb):
                    print("_", end="")
                print("\n")
                print(s)"""
        
        normal_split = [i.split("\t") for i in self.comp_data[0]]
        return normal_split
        

    def print_to_csv(self, comp_data, fname_to_be, level):
        with open(f"eredmenyek/csv/{fname_to_be}_{level}.csv", "a") as f:
            for s in self.comp_data[1]:
                f.write(f"{s}\n")
        if level == "ner":
            with open(f"eredmenyek/csv/{fname_to_be}_onlyner.csv", "a") as f:
                for s in self.comp_data[3]:
                    f.write(f"{s}\n")
            
            


