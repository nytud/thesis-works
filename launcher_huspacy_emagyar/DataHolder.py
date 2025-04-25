class DataHolder:
    def __init__(self):
        self.tok_res = []
        self.morph_res = []
        self.lem_res = []
        self.pos_res = []
        self.dep_res = []
        self.ner_res = []
    


    def print_normal(self, comp_data, level):
        normal_split = [i.split("\t") for i in comp_data[0] if i != []]        

        if len(comp_data[2]) > 0:
            normal_onlyner_split = [i.split("\t") for i in comp_data[2]]

            normal_split += normal_onlyner_split

        if level == "tok":
            self.tok_res.append(normal_split)
        elif level == "morph":
            self.morph_res.append(normal_split)
        elif level == "lem":
            self.lem_res.append(normal_split)
        elif level == "pos":
            self.pos_res.append(normal_split)
        elif level == "dep":
            self.dep_res.append(normal_split)
        elif level == "ner":
            self.ner_res.append(normal_split)
        


    def print_to_csv(self, comp_data, fname_to_be, level):
        with open(f"eredmenyek/csv/{fname_to_be}_{level}.csv", "w") as f:
            headline = comp_data[1][0]
            headline = headline.replace("\t", ",")
            f.write(headline)
            if level != "tok":
                f.write(',"HuSpaCy token","e-magyar token"')
            f.write("\n")
            for s in comp_data[1][1:]:
                f.write(f"{s}\n")
        if level == "ner":
            with open(f"eredmenyek/csv/{fname_to_be}_onlyner.csv", "w") as f:
                for s in comp_data[3]:
                    f.write(f"{s}\n")



            
            


