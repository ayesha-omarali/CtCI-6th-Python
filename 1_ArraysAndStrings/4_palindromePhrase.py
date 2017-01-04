'''
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin- drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters.The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat". "atco cta". etc.)
'''
import unittest

def isPalindrome(INPUT):
    INPUT = INPUT.replace(" ", "").lower()
    dic = {}
    for i in INPUT:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1
    if len(INPUT) % 2 == 0:
        if all(value % 2 == 0 for value in set(dic.values())):
            return True
    else:
        vals = dic.values()
        if vals.count(1) == 1:
            vals.remove(1)
            if all(value % 2 == 0 for value in set(vals)):
                return True
    return False

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = isPalindrome(test_string)
            print "Testing: {}, {}, {}".format(test_string, actual, expected)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
