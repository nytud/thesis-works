from packages.huspacy_emmorph import *
#from packages.regi_morphok.morph_orig.huspacy_emmorph_orig import *
#from packages.regi_morphok.morph2.huspacy_emmorph_morph2 import *
#from packages.regi_morphok.morph3.huspacy_emmorph_morph3 import *
#from packages.regi_morphok.morph4.huspacy_emmorph_morph4 import *
#from packages.regi_morphok.morph5.huspacy_emmorph_morph5 import *


def huspacy(txt, fname, outh, h_tokens, h_lems, h_lems_em, h_udmorph, h_emm, h_ners, h_only_ners, h_pos, h_tag, h_udpos, h_dep, h_head):
    import hu_core_news_lg

    #run huspacy
    nlp = hu_core_news_lg.load()
    nlp.add_pipe("emmorph")
    doc = nlp(txt)
    f = open('./eredmenyek/huspacy/ana_huspacy_' + fname, 'w')
    for token in doc:
        if not token.is_space: #leave out analysis for whitespace tokens
            #write into result file
            f.write(str(token.text) + '\t' + str(token.lemma_) + '\t' + str(token._.em_lemma) + '\t' + str(token._.ud_tag) + '\t' + str(token._.em_tag) + '\t' + str(token._.ud_morph) + '\t' + str(token.pos_) + '\t' + str(token.tag_) + '\t' + str(token.dep_) + '\t' + str(token.head) + '\t' + str(token.ent_iob_) + '\t' + str(token.ent_type_) + '\n')

            #fill uo the stateholder lists
            h_tokens.append(token.text)
            h_lems.append(token.lemma_)
            h_lems_em.append(token._.em_lemma)
            h_udmorph.append(str(token._.ud_morph))
            h_emm.append(str(token._.em_tag))
            h_pos.append(token.pos_)
            h_tag.append(token.tag_)
            h_udpos.append(str(token._.ud_tag))
            h_dep.append(token.dep_)
            if("\n" in str(token.head)):
                h_head.append("HEAD IS WHITESPACE!") #correct \n heads
            else:
                h_head.append(token.head)
            if(token.ent_iob_ != "O"):
                h_ners.append(token.ent_iob_ + "-" + token.ent_type_) #prepare iob result for later processing in ner comparator
            else:
                h_ners.append(token.ent_iob_)
            
    
    #collecting data for ner-centered printout
    f.write("\n")
    for ent in doc.ents:
        #not necessary: ner-centered printout can be in the result file optionally
        #f.write(str(ent.text) + '\t' + str(ent.start_char) + '\t' + str(ent.end_char) + '\t' + str(ent.label_) + '\n')
        h_only_ners.append(str(ent.text) + '\t' + str(ent.label_))

    f.close()

    #if outh is configured, print the result out
    if(outh):
        f = open('./eredmenyek/huspacy/ana_huspacy_' + fname, 'r')
        print(f.read())
        f.close()

    return h_tokens, h_lems, h_lems_em, h_udmorph, h_emm, h_ners, h_only_ners, h_pos, h_tag, h_udpos, h_dep, h_head


