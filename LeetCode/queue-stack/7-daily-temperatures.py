"""
URL: https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1363/

Problem Statement:
------------------
Given an array of integers temperatures represents the daily temperatures, return an array 
answer such that answer[i] is the number of days you have to wait after the ith day to get 
a warmer temperature. If there is no future day for which this is possible, keep 
answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:
1 <= temperatures.length <= 10^5
30 <= temperatures[i] <= 100
"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ll = len(temperatures)
        result = [0] * ll
        if ll == 1:
            return result
        stack = [(temperatures[-1], ll - 1)]
        for i in range(ll - 2, -1, -1):
            while stack:
                if stack[-1][0] > temperatures[i]:
                    result[i] = stack[-1][1] - i
                    break
                stack.pop()
            stack.append((temperatures[i], i))
        return result


"""
Testing:
--------
"""
input_list = [
    [[73, 74, 75, 71, 69, 72, 76, 73]],
    [[30, 40, 50, 60]],
    [[30, 60, 90]],
    [[30]],
    [[45, 44, 43, 43, 43, 44, 42]],
    [[30, 30, 30, 30, 30]],
]
output_list = [
    [1, 1, 4, 2, 1, 1, 0, 0],
    [1, 1, 1, 0],
    [1, 1, 0],
    [0],
    [0, 0, 3, 2, 1, 0, 0],
    [0, 0, 0, 0, 0],
]

for i in range(len(input_list)):
    result = Solution().dailyTemperatures(*input_list[i])
    print(result, output_list[i])
    assert result == output_list[i]
