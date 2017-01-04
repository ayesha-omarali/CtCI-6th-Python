'''
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
'''
import unittest

def isUnique_method1(STRING):
    '''
    This runs in O(N) time, and utilizes Python's set() function
    '''
    s = ''.join(set(list(STRING)))
    if len(STRING) == len(s):
        return True
    return False

def isUnique_method2(STRING):
    '''
    This runs in O(N) time, and keeps track of visited by simply
    adding it to a list.
    '''
    visited = []
    for i in STRING:
        if i in visited:
            return False
        if i not in visited:
            visited = visited + [i]
    return True

def isUnique_method3(STRING):   #O(N)
    '''
    This runs in O(N) time, and keeps track of the unicode
    of each character, changes True in the array once visited
    '''
    char_set = [False for _ in range(128)] #assuming ASCII chars
    for char in STRING:
        val = ord(char)
        if char_set[val]:
            return False
        char_set[val] = True
    return True

class Test(unittest.TestCase):
    test_True = [('abcd'), ('hacking'), ('love'), ('')]
    test_False = [('1337'), ('amiga'), ('2ufg =324 234')]

    def test_unique(self):
        print "Testing method1..."
        for test_string in self.test_True:
            actual = isUnique_method1(test_string)
            self.assertTrue(actual)
        for test_string in self.test_False:
            actual = isUnique_method1(test_string)
            self.assertFalse(actual)

        print "Testing method2..."
        for test_string in self.test_True:
            actual = isUnique_method2(test_string)
            self.assertTrue(actual)
        for test_string in self.test_False:
            actual = isUnique_method2(test_string)
            self.assertFalse(actual)

        print "Testing method2..."
        for test_string in self.test_True:
            actual = isUnique_method3(test_string)
            self.assertTrue(actual)
        for test_string in self.test_False:
            actual = isUnique_method3(test_string)
            self.assertFalse(actual)

if __name__ == '__main__':
    unittest.main()


