"""
URL: https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1374/

Problem Statement:
------------------
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""
from typing import List
import queue


class Solution:

    def __init__(self) -> None:
        self.visited = set()

    def get_lands(self, grid, x, y):
        result = []
        m, n = len(grid), len(grid[0])
        if x < m - 1:
            if grid[x+1][y] == '1' and (x+1, y) not in self.visited:
                result.append((x+1, y))
                self.visited.add((x+1, y))

        if x > 0:
            if grid[x-1][y] == '1' and (x-1, y) not in self.visited:
                result.append((x-1, y))
                self.visited.add((x-1, y))

        if y > 0:
            if grid[x][y-1] == '1' and (x, y-1) not in self.visited:
                result.append((x, y-1))
                self.visited.add((x, y-1))

        if y < n - 1:
            if grid[x][y+1] == '1' and (x, y+1) not in self.visited:
                result.append((x, y+1))
                self.visited.add((x, y+1))
        return result

    def numIslands(self, grid: List[List[str]]) -> int:
        q = queue.Queue()
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in self.visited and grid[i][j] == '1':
                    q.put((i, j))
                    while not q.empty():
                        item = q.get()
                        for coordinate in self.get_lands(grid, item[0], item[1]):
                            q.put(coordinate)
                    num += 1
        return num


"""
Testing:
--------
"""
input_list = [
    [[
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]],
    [[
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]],
    [[
        ["1", "1", "1"],
        ["0", "1", "0"],
        ["1", "1", "1"]
    ]]
]
output_list = [
    1,
    3,
    1,
]

for i in range(len(input_list)):
    result = Solution().numIslands(*input_list[i])
    print(result, output_list[i])
    assert result == output_list[i]
