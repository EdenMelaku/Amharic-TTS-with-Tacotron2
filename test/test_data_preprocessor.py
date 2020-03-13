import unittest
from DataPreprocessor.Abbrivations import Abbrivations

class AbbrivationTest(unittest.TestCase):

    # Returns True or False.

    def test__Abb(self):
        abrF = Abbrivations("ህ/ቁ")
        abrNF=Abbrivations("ቁ/ህ")
        self.assertEqual(abrF.lookup(), "ህዝባር ቁጥር")
        self.assertEqual(abrNF.lookup(), 0)


if __name__ == '__main__':
    unittest.main()