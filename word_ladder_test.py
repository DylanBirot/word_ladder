import unittest
import word_ladder


class TestWordLadderFunctions(unittest.TestCase):

    def test_file_load(self):
        result = word_ladder.file_load()
        return self.assertTrue(len(result) != 0)



if __name__ == '__main_':
    unittest.main()