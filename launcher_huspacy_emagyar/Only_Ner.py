class Only_Ner:
    def __init__(self, huspacy, emagyar):
        self.huspacy = huspacy
        self.emagyar = emagyar

    def to_print(self, comp_data):
        h_dict = {}
        e_dict = {}

        for h in self.huspacy.only_ner:
            h1 = h.split('\t')[0]                           #the named entity
            h2 = h.split('\t')[1]                           #its type
            if(h1 not in h_dict):
                h_dict[h1] = {h2}                           #add new named entity
            else:
                h_dict[h1].add(h2)                          #add the new type to the typelist of the existing named entity

        for e in self.emagyar.only_ner:
            e1 = e.split('\t')[0]                           #the named entity
            e2 = e.split('\t')[1]                           #its type
            if(e1 not in e_dict):
                e_dict[e1] = {e2}                           #add new named entity
            else:
                e_dict[e1].add(e2)                          #add the new type to the typelist of the existing named entity
        


        only_h = list([])                                                      #the named entity was only found by huspacy
        only_e = list([])                                                      #the named entity was only found by emagyar
        only_h_csv = list([])                                                      #the named entity was only found by huspacy
        only_e_csv = list([])  


        comp_data[2].append("összehasonlítás\tnévelem\tHuSpaCy típus\te-magyar típus")
        comp_data[3].append('"összehasonlítás","névelem","HuSpaCy típus","e-magyar típus"')

        #matching the emagyar entities to huspacy entities
        for (kh, vh) in h_dict.items():
            if(kh in e_dict):                                                  #found corresponding entity
                comp_data[2].append(f"{vh == e_dict[kh]}\t{kh}\t{vh}\t{e_dict[kh]}")         #comparing
                comp_data[3].append(f'"{vh == e_dict[kh]}","{kh}","{vh}","{e_dict[kh]}"')
            else:
                only_h.append(f"{kh}\t{vh}")                                   #not found corresponding entity
                only_h_csv.append(f'"{kh}","",{vh}')
        
        #matching the huspacy entities to emagyar entities
        for (ke, ve) in e_dict.items():
            if(ke not in h_dict):
                only_e.append(f"{ke}\t{ve}")                                   #only not found check is enough because the intersection had to be handled from the huspacy side already
                only_e_csv.append(f'"","{ke}","{ve}"')

        #print the remains
        comp_data[2].append("HuSpaCy maradék:")
        comp_data[3].append("HuSpaCy maradék:")
        for h in only_h:
            comp_data[2].append(h)
        for h in only_h_csv:
            comp_data[3].append(h)

        comp_data[2].append("e-magyar maradék:")
        comp_data[3].append("e-magyar maradék:")
        for e in only_e:
            comp_data[2].append(e)
        for e in only_e_csv:
            comp_data[3].append(e)
        
