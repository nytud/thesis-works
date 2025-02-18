import json

converter = {
    "acl":"ATT",
    "advcl":"ATT",
    "advmod":"NEG", #?
    "advmod:locy":"LOCY",
    "advmod:mode":"MODE",
    "advmod:que":"QUE",
    "advmod:tfrom":"TFROM",
    "advmod:tlocy":"TLOCY",
    "advmod:to":"TO",
    "advmod:tto":"TTO",
    "amod:att":"ATT",
    "amod:attlvc":"ATT",
    "appos":"MODE",
    "aux":"AUX",
    "case":"MODE", # az összes lehetne: LOCY, QUE, TFROM, TLOCY, TO, TTO, FROM; ha ide nem a FROM-ot írom, az teljesen kimarad, de nem lenne korrekt
    "cc":"COORD",
    "ccomp":"MODE", # az összes lehetne: LOCY, QUE, TFROM, TLOCY, TO, TTO, FROM
    "ccomp:obj":"OBJ", # itt is lehetne sok más, mindenféle ki tudja fejezni
    "ccomp:obl":"OBL", 
    "ccomp:pred":"PRED",
    "compound":"NUM", #valószínűség alapján
    "compound:preverb":"PREVERB",
    "conj":"CONJ",
    "cop":"AUX",
    "csubj":"SUBJ",
    "dep":"DEP",
    "det":"DET",
    "discourse":"DEP", # lehetne jobb is
    "dislocated":"DEP",
    "fixed":"NUM", # de csak mert 1 instance van; egyébként inkább dep lehetne
    "flat:name":"NE",
    "goeswith":"AUX", #?
    "iobj":"DAT",
    "list":"DEP", #?
    "mark":"DEP",
    "nmod":"MODE", #??
    "nmod:att":"ATT",
    "nmod:attlvc":"ATT",
    "nmod:obl":"OBL",
    "nsubj":"SUBJ",
    "nsubj:lvc":"SUBJ",
    "nummod":"NUM",
    "obj":"OBJ",
    "obj:lvc":"OBJ",
    "obl":"OBL",
    "obl:lvc":"OBL",
    "orphan":"DEP",
    "parataxis":"DEP",
    "punct":"PUNCT",
    "ROOT":"ROOT",
    "vocative":"ATT", #véleményes
    "xcomp":"INF"
}

json_str = json.dumps(converter)


def convert(ud):
    return converter[ud]



#Hungarian Szeged UD
#acl – clausal modifier of noun (adnominal clause)
#advcl – adverbial clause modifier
#advmod – adverbial modifier
#advmod:locy – relation between an adverb answering for the question „where?” and its parent
#advmod:mode – relation between other adverbs and their parents
#advmod:que – The question suffix -e “whether” is tagged as an interrogative adverb and attached to the verb via the advmod:que relation
#advmod:tfrom – relation between an adverb answering for the question „from when?” and its parent
#advmod:tlocy – relation between an adverb answering for the question „when?” and its parent
#advmod:to – relation between an adverb answering for the question „where to?” and its parent
#advmod:tto – relation between an adverb answering for the question „till when or by when?” and its parent
#amod:att – adjectival modifier. Adverbial uses of adjectives are marked with advmod:mode (szépen - nicely, which is marked as adjective in the Hungarian data). Other (attributive) uses of adjectives are marked with amod:att
#amod:attlvc – participle in a light-verb construction
#appos – appositional modifier
#aux – auxiliary
#case – case marking
#cc – coordinating conjunction
#ccomp – clausal complement
#ccomp:obj – direct object complement. The ccomp:obj relation marks an a clausal complement cross-referenced by a direct object marker.
#ccomp:obl – clausal complement (non-object); clauses that express a core dependent of the main verb but are not objects are marked with ccomp:obl
#ccomp:pred – clausal complement (predicative); clauses that express a predicative dependent of the main verb are marked with ccomp:pred
#compound – compound
#compound:preverb – relation between verb and preverb. The relation compound:preverb holds between the preverb and its parent verb whenever they are spelt in two words (nem jött el - not come-PAST-3SG-INDEF away - “he did not come”). Note that if the preverb is spelt as a separate word, it may actually occur after its verb.
#conj – conjunct
#cop – copula
#csubj – clausal subject
#dep – unspecified dependency
#det – determiner
#discourse – discourse element
#dislocated – dislocated elements
#fixed – fixed multiword expression
#flat:name – The flat:name relation is a specialization of flat used for names.
#goeswith – goes with
#iobj – indirect object
#list – list
#mark – marker
#nmod – nominal modifier
#nmod:att – nominal modifier without postposition. nmod denotes the head noun of postpositional phrases. nmod:att denotes nominal dependents of other nouns, e.g. in a possessive structure
#nmod:attlvc – object nominal in a nominalized light-verb construction
#nmod:obl – nominal modifier in oblique case. nmod denotes the head noun of postpositional phrases. nmod:obl denotes nominal modifiers (of nominals) that bear a case marker different from accusative or dative
#nsubj – nominal subject
#nsubj:lvc – subject in a light-verb construction
#nummod – numeric modifier
#obj – object
#obj:lvc – object of a light verb
#obl – oblique nominal
#obl:lvc – oblique nominal in a light-verb construction
#orphan – orphan
#parataxis – parataxis
#punct – punctuation
#root – root
#vocative – vocative
#xcomp - open clausal complement

####################################################################################################################
#Eredeti, általános UD
#acl: clausal modifier of noun (adnominal clause)
#acl:relcl: relative clause modifier
#advcl: adverbial clause modifier
#advcl:relcl: adverbial relative clause modifier
#advmod: adverbial modifier
#advmod:emph: emphasizing word, intensifier
#advmod:lmod: locative adverbial modifier
#amod: adjectival modifier
#appos: appositional modifier
#aux: auxiliary
#aux:pass: passive auxiliary
#case: case marking
#cc: coordinating conjunction
#cc:preconj: preconjunct
#ccomp: clausal complement
#clf: classifier
#compound: compound
#compound:lvc: light verb construction
#compound:prt: phrasal verb particle
#compound:redup: reduplicated compounds
#compound:svc: serial verb compounds
#conj: conjunct
#cop: copula
#csubj: clausal subject
#csubj:outer: outer clause clausal subject
#csubj:pass: clausal passive subject
#dep: unspecified dependency
#det: determiner
#det:numgov: pronominal quantifier governing the case of the noun
#det:nummod: pronominal quantifier agreeing in case with the noun
#det:poss: possessive determiner
#discourse: discourse element
#dislocated: dislocated elements
#expl: expletive
#expl:impers: impersonal expletive
#expl:pass: reflexive pronoun used in reflexive passive
#expl:pv: reflexive clitic with an inherently reflexive verb
#fixed: fixed multiword expression
#flat: flat expression
#flat:foreign: foreign words
#flat:name: names
#goeswith: goes with
#iobj: indirect object
#list: list
#mark: marker
#nmod: nominal modifier
#nmod:poss: possessive nominal modifier
#nmod:tmod: temporal modifier
#nsubj: nominal subject
#nsubj:outer: outer clause nominal subject
#nsubj:pass: passive nominal subject
#nummod: numeric modifier
#nummod:gov: numeric modifier governing the case of the noun
#obj: object
#obl: oblique nominal
#obl:agent: agent modifier
#obl:arg: oblique argument
#obl:lmod: locative modifier
#obl:tmod: temporal modifier
#orphan: orphan
#parataxis: parataxis
#punct: punctuation
#reparandum: overridden disfluency
#root: root
#vocative: vocative
#xcomp: open clausal complement






#APPEND – non-integral parts of sentences - kimarad

#ATT – relation between noun and adjective, postposition and noun, noun/nominal modifier and noun  
#AUX – relation between verb and auxiliary 

#AUXS – node representing the whole sentence - kimarad

#CONJ – conjunction 
#COORD – coordination 
#DAT – dative (suffix -nAk) 
#DET – relation between noun and determiner 

#FROM – adverb or postpositional  phrase answering for the question „from where?” - kimarad

#INF – infinitive 
#LOCY –  adverb or postpositional phrase answering for the question „where?” 
###MODE – other adverbs or postpositional phrases 
#NEG – negative 
#OBJ – relation between verb and object 
#OBL  –  relation  between  verb  and  its  other  nominal argument 
#PRED – relation between verb and nominal predicate 
#PREVERB – relation between verb and preverb 
#PUNCT – punctuation mark 
#QUE – question word
#ROOT – main element of the sentence 
#SUBJ – relation between verb and subject 
#TFROM – adverb or postpositional phrase answering for the question „from when?” 
#TLOCY – adverb or postpositional phrase answering for the question „when?” 
#TO – adverb or postpositional  phrase answering for the question „where to?” 
#TTO – adverb or postpositional phrase answering for the question „till when or by when?” 
#############A cikk szerint nincs, de az eredmények között mégis van:##############################x
#NUM - numeric
#NE - named entity
#DEP - (dependency)