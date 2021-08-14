"""
URL: https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1371/

Problem Statement:
------------------
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

Constraints:
1 <= n <= 10^4
"""
from typing import List
import queue


class Solution:

    def __init__(self) -> None:
        self.visited = set()

    def numSquares(self, n: int) -> int:
        q = queue.Queue()
        q.put((0, 0))
        self.visited.add(0)

        while q.empty() is False:
            current, count = q.get()
            i = 1
            summ = current + i * i
            count += 1
            while summ <= n:
                if summ in self.visited:
                    i += 1
                    summ = current + i * i
                    continue
                elif summ == n:
                    return count
                q.put((summ, count))
                self.visited.add(summ)
                i += 1
                summ = current + i * i
        return -1


"""
Testing:
--------
"""
input_list = [
    [12],
    [13],
    [1],
    [4],
]
output_list = [
    3,
    2,
    1,
    1,
]

for i in range(len(input_list)):
    result = Solution().numSquares(*input_list[i])
    print(result, output_list[i])
    assert result == output_list[i]
