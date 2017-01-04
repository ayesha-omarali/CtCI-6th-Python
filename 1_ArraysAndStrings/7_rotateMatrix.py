'''
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. (an you do this in place?
'''
import unittest

def rotate_matrix(matrix):
    x = len(matrix)
    result = [[0]*x for i in range(x)]
    for i, j in zip(range(x), range(x-1, -1, -1)):
        for k in range(x):
            result[k][i] = matrix[j][k]
    return result



class Test(unittest.TestCase):
    data = [

            ([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ], [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
         ]),

        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])
    ]





    def test_rotate_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = rotate_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
