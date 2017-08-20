import unittest
import word_ladder


class Test_Word_Ladder(unittest.TestCase):


    def test_file_load(self):
        self.assertEqual(word_ladder.file_load("test"), "\n\n The file name you have entered cannot be found -_- \n\n")



    def test_start_word_check(self):
        self.assertEqual(word_ladder.start_word_check("lead"), "lead")



    def test_target_word_check(self):
        self.assertEqual(word_ladder.start_word_check("gold"), "gold")



    def test_path_selection(self):
        self.assertEqual(word_ladder.path_selection("s"), True)


    def test_forbidden_build(self):
        result = word_ladder.forbidden_build("head, bead, mead")
        self.assertTrue(type(result) is list)



    def test_same(self):
        self.assertTrue(word_ladder.same("ate", "are") == 2)
        self.assertEqual(word_ladder.same("eat", "ate"), 0)
        self.assertEqual(word_ladder.same("test", "testing"), 4)
        self.assertEqual(word_ladder.same("1", "1"), 1)
        self.assertRaises(TypeError, word_ladder.same("test", "find"), 1)



    def test_build(self):
        self.assertFalse(word_ladder.build(".ead", "bead, mead, dead, head, lead", {"lead": True}, []) == False)


    def test_find(self):
        self.assertTrue(word_ladder.find("lead", "lead, load, goad, gold", {"lead" : True}, "gold", ["lead"]) == False )





if __name__ == '__main__':
    unittest.main()