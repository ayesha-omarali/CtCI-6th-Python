'''
String Compression: Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).
'''
import unittest

def string_compression(INPUT):
    strings = []
    char = INPUT[0]
    for i in range(1, len(INPUT)+1):
        if i == len(INPUT):
            strings = strings + [char]
        elif INPUT[i] == INPUT[i-1]:
            char = char + INPUT[i]
        else:
            strings = strings + [char]
            char = INPUT[i]
    result = ''.join([x[0]+str(len(x)) for x in strings])
    if len(result) < len(INPUT):
        return result
    return INPUT


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
