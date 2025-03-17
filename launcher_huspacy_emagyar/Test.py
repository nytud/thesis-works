import unittest
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


if __name__ == '__main__':
    unittest.main()