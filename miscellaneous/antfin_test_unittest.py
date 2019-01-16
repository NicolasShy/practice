import unittest

from recursive_antfin_test import no_name

class TestNoName(unittest.TestCase):

    def test_different_length(self):
        str1 = "asdfghkljljlhlkj"
        str2 = "asdlfkhooihdfg"
        self.assertFalse(no_name(str1, str2))
    
    def test_same_length_different_character(self):
        str1 = "abcdefg"
        str2 = "hijklmn"
        self.assertFalse(no_name(str1, str2))

    def test_extreme_condition1(self):
        str1 = ""
        str2 = ""
        self.assertTrue(no_name(str1, str2))

    def test_extreme_condition2(self):
        str1 = "122232131354345sdahjsdflfhgopiqyhpw3ty03yth4idhfheoyfgy3 \
        q04ty0hergihedofghosdhfposhopfygoyt9834yt98y3"
        str2 = ""
        self.assertFalse(no_name(str1, str2))

    def test_true_condition(self):
        str1 = "abcdefg"
        str2 = "gfecdba"
        self.assertTrue(no_name(str1, str2))

if __name__ == '__main__':
    unittest.main()