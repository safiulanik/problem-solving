"""
URL: https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/

Problem Statement:
------------------
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []

Constraints:
0 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5
"""
from typing import List


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ll = len(nums)
        res = []
        for i in range(ll):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = nums[i] * -1
            s, e = i+1, ll - 1
            while s < e:
                if nums[s] + nums[e] == target:
                    res.append([nums[i], nums[s], nums[e]])
                    s += 1
                    while s < e and nums[s] == nums[s-1]:
                        s += 1
                elif nums[s] + nums[e] < target:
                    s += 1
                else:
                    e -= 1
        return res


"""
Testing:
--------
[-2, -1, 1, 2]
-2, -1, 1
-2, -1, 2
-1, 1, 2
"""
input_list = [
    [[-1, 0, 1, 2, -1, -4]],
    [[]],
    [[0]],
    [[1, 2, 3, -2, -1]],
    [[0, 0, 0, 0]],
    [[1, 2, -2, -1]],
    [[0, 0, 0]],
    [[-2, 0, 1, 1, 2]],
]
output_list = [
    [[-1, -1, 2], [-1, 0, 1]],
    [],
    [],
    [[-2, -1, 3]],
    [[0, 0, 0]],
    [],
    [[0, 0, 0]],
    [[-2, 0, 2], [-2, 1, 1]],
]

for i in range(len(input_list)):
    result = Solution().threeSum(*input_list[i])
    print(result, output_list[i])
    assert result == output_list[i]
