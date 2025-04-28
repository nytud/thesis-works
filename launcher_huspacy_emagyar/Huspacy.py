from packages.huspacy_emmorph import *
#from packages.regi_morphok.morph_orig.huspacy_emmorph_orig import *
#from packages.regi_morphok.morph2.huspacy_emmorph_morph2 import *
#from packages.regi_morphok.morph3.huspacy_emmorph_morph3 import *
#from packages.regi_morphok.morph4.huspacy_emmorph_morph4 import *
#from packages.regi_morphok.morph5.huspacy_emmorph_morph5 import *

import hu_core_news_lg

class Huspacy:
    def __init__(self):
        self.tok = []
        self.morph = []
        self.morph_ud = []
        self.morph_em = []
        self.lem = []
        self.lem_em = []
        self.pos = []
        self.tag = []
        self.pos_ud = []
        self.dep = []
        self.head = []
        self.ner = []
        self.only_ner = []

    def run(self, fname, txt):
        #for simulation COMMENT FROM HERE
        nlp = hu_core_news_lg.load()
        nlp.add_pipe("emmorph")
        doc = nlp(txt)

        
        try:
            with open(f"eredmenyek/huspacy/ana_huspacy_{fname}", 'w') as f:
                f.write("token\tem_tag\tud_morph\tlemma\tem_lemma\tud_tag\tpos\ttag\tdep\thead\tent_iob\tent_type\n")
                for token in doc:
                    if not token.is_space: #leave out analysis for whitespace tokens
                        #write into result file
                        f.write(f"{token.text}\t{token._.em_tag}\t{token._.ud_morph}\t{token.lemma_}\t{token._.em_lemma}\t{token._.ud_tag}\t{token.pos_}\t{token.tag_}\t{token.dep_}\t{token.head}\t{token.ent_iob_}\t{token.ent_type_}\t\n")

                        #fill the feature lists
                        self.tok.append((token.text))
                        self.lem.append((token.lemma_))
                        self.lem_em.append((token._.em_lemma))
                        self.morph_ud.append((str(token._.ud_morph)))
                        self.morph_em.append((str(token._.em_tag)))
                        self.pos.append((token.pos_))
                        self.tag.append((token.tag_))
                        self.pos_ud.append((str(token._.ud_tag)))
                        self.dep.append((token.dep_))
                        if("\n" in str(token.head)):
                            self.head.append(("HEAD IS WHITESPACE!")) #correct \n heads
                        else:
                            self.head.append((token.head))
                        if(token.ent_iob_ != "O"):
                            self.ner.append((f"{token.ent_iob_}-{token.ent_type_}")) #prepare iob result for later processing in ner comparator
                        else:
                            self.ner.append((token.ent_iob_))
                
        
                #collecting data for ner-centered printout
                f.write("\n")
                for ent in doc.ents:
                    f.write(str(ent.text) + '\t' + str(ent.start_char) + '\t' + str(ent.end_char) + '\t' + str(ent.label_) + '\n')
                    self.only_ner.append(f"{ent.text}\t{ent.label_}")

        except Exception as e:
            raise Exception(f"Hiba a HuSpaCy nyers elemzési fájljának összeállításakor: {e}")
        
        #for simulation UNCOMMENT FROM HERE
        """
        try:
            with open(f"eredmenyek/huspacy/ana_huspacy_{fname}", 'r') as f:
                lines = f.readlines()
                for line in lines[1:]:
                    line_split = line.split('\t')
                    toname = ""
                    if len(line_split) == 13: #cut off trailing lines
                        self.tok.append(line_split[0])
                        self.lem.append(line_split[3])
                        self.lem_em.append(line_split[4])
                        self.morph_ud.append(line_split[2])
                        self.morph_em.append(line_split[1])
                        self.pos.append(line_split[6])
                        self.tag.append(line_split[7])
                        self.pos_ud.append(line_split[5])
                        self.dep.append(line_split[8])
                        self.head.append(line_split[9])
                        if line_split[10] == "O":
                            self.ner.append(line_split[10])
                        else:
                            self.ner.append(f"{line_split[10]}-{line_split[11]}")
                    if len(line_split) == 4:
                        self.only_ner.append(f"{line_split[0]}\t{line_split[3][:-1]}")
            
                        
                    
        except Exception as e:
            raise Exception(f"Hiba a HuSpaCy nyers elemzési fájljának összeállításakor: {e}")
        """ 
        #uncommentable simulation section ends here
                    

    def print(self, fname):
        ret = []
        with open(f"eredmenyek/huspacy/ana_huspacy_{fname}", 'r') as f:
            for line in f.readlines():
                ret.append(line.split("\t"))
        return ret
            
        
