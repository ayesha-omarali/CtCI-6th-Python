'''
Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
'''
#O(N)
import unittest

def isPermutation(string):
    s1, s2 = sorted(string[0]), sorted(string[1])
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)-1):
        if s1[i] != s2[i]:
            return False
    return True

class Test(unittest.TestCase):
    dataT = [(['abcd', 'bacd']), (['3563476', '7334566']),
             (['wef34f', 'wffe34'])]
    dataF = [(['abcd', 'd2cba']), (['2354', '1234']), (['dcw4f', 'dcw5f'])]

    def test_cp(self):
        # true check
        for test_string in self.dataT:
            actual = isPermutation(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = isPermutation(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()
