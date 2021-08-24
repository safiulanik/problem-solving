"""
URL: https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/777/

Problem Statement:
------------------
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

You must do it in place.

Example 1:
----------------
1 1 1      1 0 1
1 0 1  ->  0 0 0
1 1 1      1 0 1
----------------
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
--------------------
0 1 2 0      0 0 0 0
3 4 5 2  ->  0 4 5 0
1 3 1 5      0 3 1 0
--------------------
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-2^31 <= matrix[i][j] <= 2^31 - 1

Follow up:
A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""
from typing import List


class Solution:

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # """Approach 1: Using additional memory"""
        # m, n = len(matrix), len(matrix[0])
        # zeroes = set()
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             zeroes.add((i, j))
        # for tuple in zeroes:
        #     i, j = tuple
        #     # top
        #     for ii in range(i-1, -1, -1):
        #         matrix[ii][j] = 0
        #     # bottom
        #     for ii in range(i+1, m):
        #         matrix[ii][j] = 0
        #     # left
        #     for jj in range(j-1, -1, -1):
        #         matrix[i][jj] = 0
        #     # right
        #     for jj in range(j+1, n):
        #         matrix[i][jj] = 0

        """Approach 2: Using constant memory"""
        m, n = len(matrix), len(matrix[0])
        f_col = False
        for i in range(m):
            if matrix[i][0] == 0:
                f_col = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if 0 in [matrix[i][0], matrix[0][j]]:
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0
        if f_col:
            for i in range(m):
                matrix[i][0] = 0


"""
Testing:
--------
"""
input_list = [
    [[[1, 1, 1], [1, 0, 1], [1, 1, 1]]],
    [[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]],
]
output_list = [
    [[1, 0, 1], [0, 0, 0], [1, 0, 1]],
    [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
]

for i in range(len(input_list)):
    Solution().setZeroes(*input_list[i])
    print(input_list[i][0])
    assert input_list[i][0] == output_list[i]
