import unittest
import os
from Launcher import Launcher

class Tests(unittest.TestCase):
    def test_noarg(self):
        launcher = Launcher([])
        self.assertEqual(launcher.args, [])
        self.assertFalse(launcher.oute)
        self.assertFalse(launcher.outh)
        self.assertFalse(launcher.is_emagyar)
        self.assertFalse(launcher.is_huspacy)
        self.assertFalse(launcher.tok_comp)
        self.assertFalse(launcher.morph_comp)
        self.assertFalse(launcher.lem_comp)
        self.assertFalse(launcher.ner_comp)
        self.assertFalse(launcher.pos_comp)
        self.assertFalse(launcher.dep_comp)
        self.assertFalse(launcher.csv)

    def test_is_emagyar_onearg(self):
        launcher = Launcher(["-emagyar"])
        self.assertEqual(launcher.args, ["-emagyar"])
        self.assertFalse(launcher.oute)
        self.assertFalse(launcher.outh)
        self.assertTrue(launcher.is_emagyar)
        self.assertFalse(launcher.is_huspacy)
        self.assertFalse(launcher.tok_comp)
        self.assertFalse(launcher.morph_comp)
        self.assertFalse(launcher.lem_comp)
        self.assertFalse(launcher.ner_comp)
        self.assertFalse(launcher.pos_comp)
        self.assertFalse(launcher.dep_comp)
        self.assertFalse(launcher.csv)

    def test_is_huspacy_onearg(self):
        launcher = Launcher(["-huspacy"])
        self.assertEqual(launcher.args, ["-huspacy"])
        self.assertFalse(launcher.oute)
        self.assertFalse(launcher.outh)
        self.assertFalse(launcher.is_emagyar)
        self.assertTrue(launcher.is_huspacy)
        self.assertFalse(launcher.tok_comp)
        self.assertFalse(launcher.morph_comp)
        self.assertFalse(launcher.lem_comp)
        self.assertFalse(launcher.ner_comp)
        self.assertFalse(launcher.pos_comp)
        self.assertFalse(launcher.dep_comp)
        self.assertFalse(launcher.csv)

    def test_oute_onearg(self):
        launcher = Launcher(["-oute"])
        self.assertEqual(launcher.args, ["-oute"])
        self.assertTrue(launcher.oute)
        self.assertFalse(launcher.outh)
        self.assertFalse(launcher.is_emagyar)
        self.assertFalse(launcher.is_huspacy)
        self.assertFalse(launcher.tok_comp)
        self.assertFalse(launcher.morph_comp)
        self.assertFalse(launcher.lem_comp)
        self.assertFalse(launcher.ner_comp)
        self.assertFalse(launcher.pos_comp)
        self.assertFalse(launcher.dep_comp)
        self.assertFalse(launcher.csv)

    def test_outh_onearg(self):
        launcher = Launcher(["-outh"])
        self.assertEqual(launcher.args, ["-outh"])
        self.assertFalse(launcher.oute)
        self.assertTrue(launcher.outh)
        self.assertFalse(launcher.is_emagyar)
        self.assertFalse(launcher.is_huspacy)
        self.assertFalse(launcher.tok_comp)
        self.assertFalse(launcher.morph_comp)
        self.assertFalse(launcher.lem_comp)
        self.assertFalse(launcher.ner_comp)
        self.assertFalse(launcher.pos_comp)
        self.assertFalse(launcher.dep_comp)
        self.assertFalse(launcher.csv)

    def test_tok_comp_onearg(self):
        launcher = Launcher(["-tok"])
        self.assertEqual(launcher.args, ["-tok"])
        self.assertFalse(launcher.oute)
        self.assertFalse(launcher.outh)
        self.assertFalse(launcher.is_emagyar)
        self.assertFalse(launcher.is_huspacy)
        self.assertTrue(launcher.tok_comp)
        self.assertFalse(launcher.morph_comp)
        self.assertFalse(launcher.lem_comp)
        self.assertFalse(launcher.ner_comp)
        self.assertFalse(launcher.pos_comp)
        self.assertFalse(launcher.dep_comp)
        self.assertFalse(launcher.csv)

    def test_morph_comp_onearg(self):
        launcher = Launcher(["-morph"])
        self.assertEqual(launcher.args, ["-morph"])
        self.assertFalse(launcher.oute)
        self.assertFalse(launcher.outh)
        self.assertFalse(launcher.is_emagyar)
        self.assertFalse(launcher.is_huspacy)
        self.assertFalse(launcher.tok_comp)
        self.assertTrue(launcher.morph_comp)
        self.assertFalse(launcher.lem_comp)
        self.assertFalse(launcher.ner_comp)
        self.assertFalse(launcher.pos_comp)
        self.assertFalse(launcher.dep_comp)
        self.assertFalse(launcher.csv)

    def test_lem_comp_onearg(self):
        launcher = Launcher(["-lem"])
        self.assertEqual(launcher.args, ["-lem"])
        self.assertFalse(launcher.oute)
        self.assertFalse(launcher.outh)
        self.assertFalse(launcher.is_emagyar)
        self.assertFalse(launcher.is_huspacy)
        self.assertFalse(launcher.tok_comp)
        self.assertFalse(launcher.morph_comp)
        self.assertTrue(launcher.lem_comp)
        self.assertFalse(launcher.ner_comp)
        self.assertFalse(launcher.pos_comp)
        self.assertFalse(launcher.dep_comp)
        self.assertFalse(launcher.csv)

    def test_ner_comp_onearg(self):
        launcher = Launcher(["-ner"])
        self.assertEqual(launcher.args, ["-ner"])
        self.assertFalse(launcher.oute)
        self.assertFalse(launcher.outh)
        self.assertFalse(launcher.is_emagyar)
        self.assertFalse(launcher.is_huspacy)
        self.assertFalse(launcher.tok_comp)
        self.assertFalse(launcher.morph_comp)
        self.assertFalse(launcher.lem_comp)
        self.assertTrue(launcher.ner_comp)
        self.assertFalse(launcher.pos_comp)
        self.assertFalse(launcher.dep_comp)
        self.assertFalse(launcher.csv)

    def test_pos_comp_onearg(self):
        launcher = Launcher(["-pos"])
        self.assertEqual(launcher.args, ["-pos"])
        self.assertFalse(launcher.oute)
        self.assertFalse(launcher.outh)
        self.assertFalse(launcher.is_emagyar)
        self.assertFalse(launcher.is_huspacy)
        self.assertFalse(launcher.tok_comp)
        self.assertFalse(launcher.morph_comp)
        self.assertFalse(launcher.lem_comp)
        self.assertFalse(launcher.ner_comp)
        self.assertTrue(launcher.pos_comp)
        self.assertFalse(launcher.dep_comp)
        self.assertFalse(launcher.csv)

    def test_dep_comp_onearg(self):
        launcher = Launcher(["-dep"])
        self.assertEqual(launcher.args, ["-dep"])
        self.assertFalse(launcher.oute)
        self.assertFalse(launcher.outh)
        self.assertFalse(launcher.is_emagyar)
        self.assertFalse(launcher.is_huspacy)
        self.assertFalse(launcher.tok_comp)
        self.assertFalse(launcher.morph_comp)
        self.assertFalse(launcher.lem_comp)
        self.assertFalse(launcher.ner_comp)
        self.assertFalse(launcher.pos_comp)
        self.assertTrue(launcher.dep_comp)
        self.assertFalse(launcher.csv)

    def test_csv_onearg(self):
        launcher = Launcher(["-csv"])
        self.assertEqual(launcher.args, ["-csv"])
        self.assertFalse(launcher.oute)
        self.assertFalse(launcher.outh)
        self.assertFalse(launcher.is_emagyar)
        self.assertFalse(launcher.is_huspacy)
        self.assertFalse(launcher.tok_comp)
        self.assertFalse(launcher.morph_comp)
        self.assertFalse(launcher.lem_comp)
        self.assertFalse(launcher.ner_comp)
        self.assertFalse(launcher.pos_comp)
        self.assertFalse(launcher.dep_comp)
        self.assertTrue(launcher.csv)

    def test_multiarg(self):
        launcher = Launcher(["-huspacy", "-lem", "-tok", "-oute"])
        self.assertEqual(launcher.args, ["-huspacy", "-lem", "-tok", "-oute"])
        self.assertTrue(launcher.oute)
        self.assertFalse(launcher.outh)
        self.assertFalse(launcher.is_emagyar)
        self.assertTrue(launcher.is_huspacy)
        self.assertTrue(launcher.tok_comp)
        self.assertFalse(launcher.morph_comp)
        self.assertTrue(launcher.lem_comp)
        self.assertFalse(launcher.ner_comp)
        self.assertFalse(launcher.pos_comp)
        self.assertFalse(launcher.dep_comp)
        self.assertFalse(launcher.csv)

    def test_unknown_arg(self):
        with self.assertRaises(SystemExit) as se:
            launcher = Launcher(["-huspacy", "-ner", "-unknown", "-outh"])
            self.assertEqual(se.exception, "Hiba: ismeretlen argumentum: -unknown")

    def test_mkdir_eredmenyek(self):
        launcher = Launcher(["-huspacy", "-ner", "-outh"])
        exists = os.path.exists(os.getcwd() + "/eredmenyek/")
        self.assertTrue(exists)

    def test_mkdir_huspacy(self):
        launcher = Launcher(["-huspacy", "-ner", "-outh"])
        exists = os.path.exists(os.getcwd() + "/eredmenyek/huspacy")
        self.assertTrue(exists)

    def test_mkdir_emagyar(self):
        launcher = Launcher(["-huspacy", "-ner", "-outh"])
        exists = os.path.exists(os.getcwd() + "/eredmenyek/emagyar")
        self.assertTrue(exists)

    def test_mkdir_csv(self):
        launcher = Launcher(["-emagyar", "-huspacy", "-tok", "-csv"])
        exists = os.path.exists(os.getcwd() + "/eredmenyek/csv")
        self.assertTrue(exists)

    def test_emagyar(self):
        txt = "Ez egy tesztfájl."
        with open("testfile.txt", "w") as f:
            f.write(txt)
        launcher = Launcher(["-emagyar", "testfile.txt" ])
        launcher.launch()
        exists = os.path.exists(os.getcwd() + "/eredmenyek/emagyar/ana_emagyar_testfile.txt")
        self.assertTrue(exists)

    def test_huspacy(self):
        txt = "Ez egy tesztfájl."
        with open("testfile.txt", "w") as f:
            f.write(txt)
        launcher = Launcher(["-huspacy", "testfile.txt" ])
        launcher.launch()
        exists = os.path.exists(os.getcwd() + "/eredmenyek/huspacy/ana_huspacy_testfile.txt")
        self.assertTrue(exists)

    def test_csv(self):
        txt = "Ez egy tesztfájl."
        with open("testfile.txt", "w") as f:
            f.write(txt)
        launcher = Launcher(["-emagyar", "-huspacy", "-tok", "-csv", "testfile.txt" ])
        launcher.launch()
        exists = os.path.exists(os.getcwd() + "/eredmenyek/csv/testfile_tok.csv")
        self.assertTrue(exists)



    #integration tests: the following tests aim to test the whole line of functionality in the app within a launched analysis.
    #the expected results were created by running the text processing systems separately, not with this app
    #the expected results also take the capabilities and expected conversions into consideration, so they test purely the app

    def test_tok(self):
        txt = "Ez egy tesztfájl."
        with open("testfile.txt", "w") as f:
            f.write(txt)
        launcher = Launcher(["-emagyar", "-huspacy", "-tok", "-csv", "testfile.txt" ])
        launcher.launch()  
        expected = [[
            ["HuSpaCy tokenszám: 4"], ["e-magyar tokenszám: 4"], 
            ["összehasonlítás", "HuSpaCy token", "e-magyar token"],
            ["True", "|Ez|", "|Ez|"],
            ["True", "|egy|", "|egy|"],
            ["True", "|tesztfájl|", "|tesztfájl|"], 
            ["True", "|.|", "|.|"]
        ]]
        self.assertEqual(launcher.data_holder.tok_res, expected) 

    def test_morph(self):
        txt = "Szeretek almát enni."
        with open("testfile.txt", "w") as f:
            f.write(txt)
        launcher = Launcher(["-emagyar", "-huspacy", "-morph", "-csv", "testfile.txt" ])
        launcher.launch()  
        expected = [[
            ["HuSpaCy tokenszám: 4"], ["e-magyar tokenszám: 4"], 
            ["összehasonlítás", "HuSpaCy UD morf. elemz.", "HuSpaCy EmMorph morf. elemz.", "e-magyar morf. elemz."],
            ["True", "|Definite=Ind|Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin|Voice=Act|", "|[/V][Prs.NDef.1Sg]|", "|[/V][Prs.NDef.1Sg]|", "(Szeretek Szeretek)"],
            ["True", "|Case=Acc|Number=Sing|", "|[/N][Acc]|", "|[/N][Acc]|", "(almát almát)"],
            ["True", "|VerbForm=Inf|Voice=Act|", "|[/V][Inf]|", "|[/V][Inf]|", "(enni enni)"], 
            ["False", "|None|", "|None|", "|[Punct]|", "(. .)"]
        ]]
        self.assertEqual(launcher.data_holder.morph_res, expected)   

    
    def test_lem(self):
        txt = "Szeretek almát enni."
        with open("testfile.txt", "w") as f:
            f.write(txt)
        launcher = Launcher(["-emagyar", "-huspacy", "-lem", "-csv", "testfile.txt" ])
        launcher.launch()  
        expected = [[
            ["HuSpaCy tokenszám: 4"], ["e-magyar tokenszám: 4"], 
            ["összehasonlítás", "HuSpaCy lemma", "HuSpaCy EmMorph lemma", "e-magyar lemma"],
            ["True", "|szeret|", "|szeret|", "|szeret|", "(Szeretek Szeretek)"],
            ["True", "|alma|", "|alma|", "|alma|", "(almát almát)"],
            ["True", "|eszik|", "|eszik|", "|eszik|", "(enni enni)"], 
            ["False", "|.|", "|None|", "|.|", "(. .)"]
        ]]
        self.assertEqual(launcher.data_holder.lem_res, expected)   

    
    def test_pos(self):
        txt = "Szeretek almát enni."
        with open("testfile.txt", "w") as f:
            f.write(txt)
        launcher = Launcher(["-emagyar", "-huspacy", "-pos", "-csv", "testfile.txt" ])
        launcher.launch()  
        expected = [[
            ["HuSpaCy tokenszám: 4"], ["e-magyar tokenszám: 4"], 
            ["összehasonlítás", "HuSpaCy pos", "HuSpaCy tag", "HuSpaCy EmMorph UD POS", "e-magyar POS"],
            ["True", "|VERB|", "|VERB|", "|VERB|", "|VERB|", "(Szeretek Szeretek)"],
            ["True", "|NOUN|", "|NOUN|", "|NOUN|", "|NOUN|", "(almát almát)"],
            ["True", "|VERB|", "|VERB|", "|VERB|", "|VERB|", "(enni enni)"], 
            ["False", "|PUNCT|", "|PUNCT|", "|[]|", "|PUNCT|", "(. .)"]
        ]]
        self.assertEqual(launcher.data_holder.pos_res, expected)    

    
    def test_dep(self):
        txt = "Ez egy tesztfájl."
        with open("testfile.txt", "w") as f:
            f.write(txt)
        launcher = Launcher(["-emagyar", "-huspacy", "-dep", "-csv", "testfile.txt" ])
        launcher.launch()  
        expected = [[
            ["HuSpaCy tokenszám: 4"], ["e-magyar tokenszám: 4"], 
            ["összehasonlítás (dep. elemz.)", "összehasonlítás (fej)", "HuSpaCy dep. elemz. (eredeti)", "HuSpaCy dep. elemz. (konvertált)", "HuSpaCy fej", "e-magyar dep. elemz.", "e-magyar fej"],
            ["True", "True", "|(det)|", "|DET|", "|tesztfájl|", "|DET|", "|tesztfájl|", "(Ez Ez)"],
            ["True", "True", "|(det)|", "|DET|", "|tesztfájl|", "|DET|", "|tesztfájl|", "(egy egy)"],
            ["True", "True", "|(ROOT)|", "|ROOT|", "|tesztfájl|", "|ROOT|", "|tesztfájl|", "(tesztfájl tesztfájl)"], 
            ["True", "False", "|(punct)|", "|PUNCT|", "|tesztfájl|", "|PUNCT|", "|.|", "(. .)"]
        ]]
        self.assertEqual(launcher.data_holder.dep_res, expected)   

    
    def test_ner(self):
        txt = "János Brazíliában lakik."
        with open("testfile.txt", "w") as f:
            f.write(txt)
        launcher = Launcher(["-emagyar", "-huspacy", "-ner", "-csv", "testfile.txt" ])
        launcher.launch()  
        expected = [[
            ["HuSpaCy tokenszám: 4"], ["e-magyar tokenszám: 4"], 
            ["összehasonlítás", "HuSpaCy IOB", "e-magyar IOB"],
            ["False", "|B-PER|", "|O|", "(János János)"],
            ["False", "|B-LOC|", "|O|", "(Brazíliában Brazíliában)"],
            ["True", "|O|", "|O|", "(lakik lakik)"], 
            ["True", "|O|", "|O|", "(. .)"],
            ['összehasonlítás', 'névelem', 'HuSpaCy típus', 'e-magyar típus'],
            ["HuSpaCy maradék:"],
            ["János", "{'PER'}"],
            ["Brazíliában", "{'LOC'}"],
            ["e-magyar maradék:"]
        ]]
        self.assertEqual(launcher.data_holder.ner_res, expected)   

  

if __name__ == '__main__':
    unittest.main()