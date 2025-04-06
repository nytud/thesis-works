from Huspacy import Huspacy
from Emagyar import Emagyar
from packages.dep_converter import convert

import os

class Diffsolver:
    def __init__(self, huspacy, emagyar):
        self.huspacy = huspacy
        self.emagyar = emagyar
        
        

    def solve(self, diff_to_print_e, diff_to_print_h, csv_diff_to_print_e, csv_diff_to_print_h, jj, kk, j, k, comp_data):
        modified = False
       
        if(k+kk < len(self.emagyar.tok) and j+jj < len(self.huspacy.tok)): #prevent index error
            if(k != len(self.emagyar.tok)-kk and j != len(self.huspacy.tok)-jj and  self.huspacy.tok[j+jj] == self.emagyar.tok[k+kk]): #found the next match
                if(kk > jj): #emagyar shift was greater -> huspacy is ahead -> emagyar remains are to be printed
                    for i in range (0, kk-jj):
                        dtp = diff_to_print_e.replace("_tok_", self.emagyar.tok[k])
                        dtp = dtp.replace("_morph_", self.emagyar.morph[k])
                        dtp = dtp.replace("_lem_", self.emagyar.lem[k])
                        dtp = dtp.replace("_pos_", self.emagyar.pos[k])
                        dtp = dtp.replace("_dep_", self.emagyar.dep[k])
                        dtp = dtp.replace("_head_", self.emagyar.head[k])
                        dtp = dtp.replace("_ner_", self.emagyar.ner[k])
                        comp_data[0].append("emagyar\t" + dtp)
                        
                        
                        dtp_csv = csv_diff_to_print_e.replace("_tok_", self.emagyar.tok[k])
                        dtp_csv = dtp.replace("_morph_", self.emagyar.morph[k])
                        dtp_csv = dtp.replace("_lem_", self.emagyar.lem[k])
                        dtp_csv = dtp.replace("_pos_", self.emagyar.pos[k])
                        dtp_csv = dtp.replace("_dep_", self.emagyar.dep[k])
                        dtp_csv = dtp.replace("_head_", self.emagyar.head[k])
                        dtp_csv = dtp.replace("_ner_", self.emagyar.ner[k])
                        comp_data[1].append("emagyar\t" + dtp)


                        k = k+1
                else:
                    for i in range (0, jj-kk): #huspacy shift was greater -> emagyar is ahead -> huspacy remains are to be printed
                        dtp = diff_to_print_h.replace("_tok_", self.huspacy.tok[j])
                        dtp = dtp.replace("_lem_", self.huspacy.lem[j])
                        dtp = dtp.replace("_lemem_", str(self.huspacy.lem_em[j]))
                        dtp = dtp.replace("_morphud_", str(self.huspacy.morph_ud[j]))
                        dtp = dtp.replace("_morphem_", str(self.huspacy.morph_em[j]))
                        dtp = dtp.replace("_pos_", self.huspacy.pos[j])
                        dtp = dtp.replace("_tag_", self.huspacy.tag[j])
                        dtp = dtp.replace("_posud_", self.huspacy.pos_ud[j])
                        dtp = dtp.replace("_dep_", self.huspacy.dep[j])
                        dtp = dtp.replace("_depconv_", convert(self.huspacy.dep[j]))
                        dtp = dtp.replace("_head_", str(self.huspacy.head[j]))
                        dtp = dtp.replace("_ner_", self.huspacy.ner[j])
                        comp_data[0].append("huspacy\t" + dtp)
                        

                        dtp_csv = csv_diff_to_print_e.replace("_tok_", self.emagyar.tok[k])
                        dtp_csv = dtp.replace("_morph_", self.emagyar.morph[k])
                        dtp_csv = dtp.replace("_lem_", self.emagyar.lem[k])
                        dtp_csv = dtp.replace("_pos_", self.emagyar.pos[k])
                        dtp_csv = dtp.replace("_dep_", self.emagyar.dep[k])
                        dtp_csv = dtp.replace("_head_", self.emagyar.head[k])
                        dtp_csv = dtp.replace("_ner_", self.emagyar.ner[k])
                        comp_data[1].append("huspacy\t" + dtp)

                        
                        j = j+1

                
                modified = True #means: the diffsolving is done, the original print has been modified accordingly
                #False only when diffsolver was called with wrong shift combination
                
        return j, k, modified, comp_data
