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

        




if __name__ == '__main__':
    unittest.main()