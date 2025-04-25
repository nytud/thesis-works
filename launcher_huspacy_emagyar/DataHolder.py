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
        


    def print_to_csv(self, fname_to_be, level):
        with open(f"eredmenyek/csv/{fname_to_be}_{level}.csv", "a") as f:
            for s in self.model.comp_data[1]:
                f.write(f"{s}\n")
        if level == "ner":
            with open(f"eredmenyek/csv/{fname_to_be}_onlyner.csv", "a") as f:
                for s in comp_data[3]:
                    f.write(f"{s}\n")



            
            


