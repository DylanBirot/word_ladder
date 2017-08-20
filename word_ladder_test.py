import unittest
import word_ladder


class Test_Word_Ladder(unittest.TestCase):


    def test_file_load(self):
        pass
    #test something here

    def test_start_word_check(self):
        pass
    #self.assertEqual(word_ladder.start_word_check(), "Word cannot be a number \n\n\n")


    def test_target_word_check(self):
        pass
    #self.assertEqual(word_ladder.start_word_check(), "Word cannot be a number \n\n\n")



    def test_path_selection(self):
        pass
    #test something here


    def test_forbidden_build(self):
        pass

    # test something here



    def test_same(self):
        self.assertTrue(word_ladder.same("ate", "are") == 2)
        self.assertTrue(word_ladder.same(1, 1) == TypeError)
        self.assertEqual(word_ladder.same("eat", "ate"), 0)
        self.assertEqual(word_ladder.same("test", "testing"), 4)
        self.assertEqual(word_ladder.same("1", "1"), 1)
        # self.assertRaises(TypeError, word_ladder.same(1,1))


    def test_build(self):
        pass

    # test something here


    def test_find(self):
        pass
        # test something here


if __name__ == '__main__':
    unittest.main()