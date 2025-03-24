from Huspacy import Huspacy
from Emagyar import Emagyar
from packages.dep_converter import convert

import os

class Diffsolver:
    def __init__(self, huspacy, emagyar, jj, kk, j, k, comp_data):
        self.huspacy = huspacy
        self.emagyar = emagyar
        self.jj = jj
        self.kk = kk
        self.j = j
        self.k = k
        self.comp_data = comp_data
        

    def solve(self, str_to_print, diff_to_print_e, diff_to_print_h, csv_to_print, csv_diff_to_print_e, csv_diff_to_print_h):
        modified = False
        if(self.k+self.kk < len(self.emagyar.tok) and self.j+self.jj < len(self.huspacy.tok)): #prevent index error
            if(self.k != len(self.emagyar.tok)-self.kk and self.j != len(self.huspacy.tok)-self.jj and  self.huspacy.tok[self.j+self.jj] == self.emagyar.tok[self.k+self.kk]): #found the next match
                
                if(self.kk > self.jj): #emagyar shift was greater -> huspacy is ahead -> emagyar remains are to be printed
                    for i in range (0, self.kk-self.jj):
                        dtp = diff_to_print_e.replace("_tok_", self.emagyar.tok[self.k])
                        dtp = dtp.replace("_morph_", self.emagyar.morph[self.k])
                        dtp = dtp.replace("_lem_", self.emagyar.lem[self.k])
                        dtp = dtp.replace("_pos_", self.emagyar.pos[self.k])
                        dtp = dtp.replace("_dep_", self.emagyar.dep[self.k])
                        dtp = dtp.replace("_head_", self.emagyar.head[self.k])
                        dtp = dtp.replace("_ner_", self.emagyar.ner[self.k])
                        self.comp_data[0].append("emagyar\t" + dtp)
                        
                        
                        dtp_csv = csv_diff_to_print_e.replace("_tok_", self.emagyar.tok[self.k])
                        dtp_csv = dtp.replace("_morph_", self.emagyar.morph[self.k])
                        dtp_csv = dtp.replace("_lem_", self.emagyar.lem[self.k])
                        dtp_csv = dtp.replace("_pos_", self.emagyar.pos[self.k])
                        dtp_csv = dtp.replace("_dep_", self.emagyar.dep[self.k])
                        dtp_csv = dtp.replace("_head_", self.emagyar.head[self.k])
                        dtp_csv = dtp.replace("_ner_", self.emagyar.ner[self.k])
                        self.comp_data[1].append("emagyar\t" + dtp)


                        self.k = self.k+1
                else:
                    for i in range (0, self.jj-self.kk): #huspacy shift was greater -> emagyar is ahead -> huspacy remains are to be printed
                        dtp = diff_to_print_h.replace("_tok_", self.huspacy.tok[self.j])
                        dtp = dtp.replace("_lem_", self.huspacy.lem[self.j])
                        dtp = dtp.replace("_lemem_", str(self.huspacy.lem_em[self.j]))
                        dtp = dtp.replace("_morphud_", str(self.huspacy.morph_ud[self.j]))
                        dtp = dtp.replace("_morphem_", str(self.huspacy.morph_em[self.j]))
                        dtp = dtp.replace("_pos_", self.huspacy.pos[self.j])
                        dtp = dtp.replace("_tag_", self.huspacy.tag[self.j])
                        dtp = dtp.replace("_posud_", self.huspacy.pos_ud[self.j])
                        dtp = dtp.replace("_dep_", self.huspacy.dep[self.j])
                        dtp = dtp.replace("_depconv_", convert(self.huspacy.dep[self.j]))
                        dtp = dtp.replace("_head_", str(self.huspacy.head[self.j]))
                        dtp = dtp.replace("_ner_", self.huspacy.ner[self.j])
                        self.comp_data[0].append("huspacy\t" + dtp)
                        
                        

                        dtp_csv = csv_diff_to_print_e.replace("_tok_", self.emagyar.tok[self.k])
                        dtp_csv = dtp.replace("_morph_", self.emagyar.morph[self.k])
                        dtp_csv = dtp.replace("_lem_", self.emagyar.lem[self.k])
                        dtp_csv = dtp.replace("_pos_", self.emagyar.pos[self.k])
                        dtp_csv = dtp.replace("_dep_", self.emagyar.dep[self.k])
                        dtp_csv = dtp.replace("_head_", self.emagyar.head[self.k])
                        dtp_csv = dtp.replace("_ner_", self.emagyar.ner[self.k])
                        self.comp_data[1].append("huspacy\t" + dtp)

                        
                        self.j = self.j+1

                
                modified = True #means: the diffsolving is done, the original print has been modified accordingly
                #False only when diffsolver was called with wrong shift combination

        return self.j, self.k, modified, self.comp_data
