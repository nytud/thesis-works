from spacy.tokens import Doc, Token, MorphAnalysis
from spacy.language import Language
from spacy.lang.hu import Hungarian
from spacy.morphology import Morphology
from typing import List, Tuple, Dict
from emmorph2ud2 import EmMorph2UD2
from emmorphpy import EmMorphPy

@Hungarian.factory(
    "emmorph",
    requires=["token.text"],
 )
def create_emmorph(nlp: Language, name: str) -> "EmMorphPyComponent":
    return EmMorphPyComponent(nlp, name)

class EmMorphPyComponent:
    def __init__(self, nlp: Language, name: str):
        self._nlp = nlp
        self._name = name
        self._em = EmMorphPy()
        self._converter = EmMorph2UD2()
        Token.set_extension("em_anas", default=[], force=True)
        Token.set_extension("em_tag", default=None, force=True)
        Token.set_extension("em_lemma", default=None, force=True)
        Token.set_extension("ud_tag", default=[], force=True)
        Token.set_extension("ud_anas", default=[], force=True)
        Token.set_extension("ud_morph", default=None, force=True)

    def __call__(self, doc: Doc) -> Doc:
        tok: Token
        for tok in doc:
            if not tok.is_space:
                analyses: List[Tuple[str, str]] = self._em.stem(tok)
                ud_analyses: List[Tuple[str, str]] = [self._converter.parse(str(tok), ana[0], ana[1]) for ana in analyses]
    
                tok._.em_anas = analyses
                tok._.ud_anas = ud_analyses
    
                morph_dict: Dict[str, str] = tok.morph.to_dict()
                best_sim_score = 0
                for(em_lemma, em_tag), (ud_tag, ud_morph) in zip(analyses, ud_analyses):
                    if ud_tag == tok.pos_:
                        emmorph_dict: Dict[str, str] = Morphology.feats_to_dict(ud_morph)
                        sim_score: float = sum(
                            emmorph_dict.get(key) == value
                            for key, value in morph_dict.items()
                        ) / (len(
                            set(morph_dict.keys()) | set(emmorph_dict.keys())
                        ) or 1 )
                        if sim_score > best_sim_score or str(tok.morph) == "" and ud_morph == "_":
                            tok._.em_tag = em_tag
                            tok._.ud_tag = ud_tag
                            tok._.em_lemma = em_lemma
                            tok._.ud_morph = MorphAnalysis(self._nlp.vocab, ud_morph)
                            #best_sim_score = sim_score

        return doc



