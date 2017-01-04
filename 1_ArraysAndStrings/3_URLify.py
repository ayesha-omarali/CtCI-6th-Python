'''
URLify: Write a method to replace all spaces in a string with '%20: You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string.
    Input: "Mr John Smith " J 13 Output: "Mr%20J ohn%20Smith"
'''

import unittest


def URLify(INPUT, length):
    INPUT = INPUT[:length]
    INPUT = map((lambda x:  '%20' if x == ' ' else x), INPUT)
    return ''.join(INPUT)


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        (('much ado about nothing      '), 22,
         ('much%20ado%20about%20nothing')),
        (('Mr John Smith    '), 13, ('Mr%20John%20Smith'))]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = URLify(''.join(test_string), length)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
