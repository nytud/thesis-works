class Only_Ner:
    def __init__(self, huspacy, emagyar):
        self.huspacy = huspacy
        self.emagyar = emagyar

    def print(self):
        h_dict = {}
        e_dict = {}

        for h in self.huspacy.only_ner:
            h1 = h.split('\t')[0] #the named entity
            h2 = h.split('\t')[1] #its type
            if(h1 not in h_dict):
                h_dict[h1] = {h2} #add new named entity
            else:
                h_dict[h1].add(h2) #add the new type to the typelist of the existing named entity

        for e in self.emagyar.only_ner:
            e1 = e.split('\t')[0] #the named entity
            e2 = e.split('\t')[1] #its type
            if(e1 not in e_dict):
                e_dict[e1] = {e2} #add new named entity
            else:
                e_dict[e1].add(e2) #add the new type to the typelist of the existing named entity
        


        only_h = list([]) #the named entity was only found by huspacy
        only_e = list([]) #the named entity was only found by emagyar
        #matching the emagyar entities to huspacy entities
        for (kh, vh) in h_dict.items():
            if(kh in e_dict): #found corresponding entity
                print(str(vh == e_dict[kh]) + '\t' + kh + '\t' + str(vh) + '\t' + str(e_dict[kh])) #comparing
            else:
                only_h.append(kh + '\t' + str(vh)) #not found corresponding entity
        
        #matching the huspacy entities to emagyar entities
        for (ke, ve) in e_dict.items():
            if(ke not in h_dict):
                only_e.append(ke + '\t' + str(ve)) #only not found check is enough because the intersection had to be handled from the huspacy side already

        #print the remains
        print("huspacy maradek:")
        for h in only_h:
            print(h)

        print("emagyar maradek:")
        for e in only_e:
            print(e)
        
