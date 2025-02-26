from packages.huspacy_emmorph import *
#from packages.regi_morphok.morph_orig.huspacy_emmorph_orig import *
#from packages.regi_morphok.morph2.huspacy_emmorph_morph2 import *
#from packages.regi_morphok.morph3.huspacy_emmorph_morph3 import *
#from packages.regi_morphok.morph4.huspacy_emmorph_morph4 import *
#from packages.regi_morphok.morph5.huspacy_emmorph_morph5 import *

import hu_core_news_lg

class Huspacy:
    def __init__(self):
        self.tok = list([])
        self.morph = list([])
        self.morph_ud = list([])
        self.morph_em = list([])
        self.lem = list([])
        self.lem_em = list([])
        self.pos = list([])
        self.tag = list([])
        self.pos_ud = list([])
        self.dep = list([])
        self.head = list([])
        self.ner = list([])
        self.only_ner = list([])

    def run(self, fname, txt):
        nlp = hu_core_news_lg.load()
        nlp.add_pipe("emmorph")
        doc = nlp(txt)

        with open('./eredmenyek/huspacy/ana_huspacy_' + fname, 'w') as f:
            for token in doc:
                if not token.is_space: #leave out analysis for whitespace tokens
                    #write into result file
                    f.write(str(token.text) + '\t' + str(token.lemma_) + '\t' + str(token._.em_lemma) + '\t' + str(token._.ud_tag) + '\t' + str(token._.em_tag) + '\t' + str(token._.ud_morph) + '\t' + str(token.pos_) + '\t' + str(token.tag_) + '\t' + str(token.dep_) + '\t' + str(token.head) + '\t' + str(token.ent_iob_) + '\t' + str(token.ent_type_) + '\n')

                    #fill uo the stateholder lists
                    self.tok.append(token.text)
                    self.lem.append((token.text, token.lemma_))
                    self.lem_em.append((token.text, token._.em_lemma))
                    self.morph_ud.append((token.text, str(token._.ud_morph)))
                    self.morph_em.append((token.text, str(token._.em_tag)))
                    self.pos.append((token.text, token.pos_))
                    self.tag.append((token.text, token.tag_))
                    self.pos_ud.append((token.text, str(token._.ud_tag)))
                    self.dep.append((token.text, token.dep_))
                    if("\n" in str(token.head)):
                        self.head.append(("WHITESPACE", "HEAD IS WHITESPACE!")) #correct \n heads
                    else:
                        self.head.append((token.text, token.head))
                    if(token.ent_iob_ != "O"):
                        self.ner.append((token.text, token.ent_iob_ + "-" + token.ent_type_)) #prepare iob result for later processing in ner comparator
                    else:
                        self.ner.append((token.text, token.ent_iob_))
            
    
                #collecting data for ner-centered printout
                f.write("\n")
                for ent in doc.ents:
                    #not necessary: ner-centered printout can be in the result file optionally
                    #f.write(str(ent.text) + '\t' + str(ent.start_char) + '\t' + str(ent.end_char) + '\t' + str(ent.label_) + '\n')
                    self.only_ner.append(str(ent.text) + '\t' + str(ent.label_))

    def print(self, fname):
        with open('./eredmenyek/huspacy/ana_huspacy_' + fname, 'r') as f:
            print(f.read())
        
