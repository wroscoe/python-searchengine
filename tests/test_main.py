import unittest
from pysearcher import analysis 

class TestAnalysis(unittest.TestCase):

    def test_analysis_tokenize(self):
        tokens = analysis.tokenize('this is a string')
        self.assertTrue(len(tokens) == 4)


class TestLoad(unittest.TestCase):

    def test_load_yaml(self):
        tokens = analysis.tokenize('this is a string')
        self.assertTrue(len(tokens) == 4)



if __name__ == '__main__':
    unittest.main()