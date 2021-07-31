"""
URL: https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3238/

Problem Statement:
------------------
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2

Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mco = 0
        tmco = 0
        for i in nums:
            if i == 1:
                tmco += 1
            else:
                mco = max(mco, tmco)
                tmco = 0

        return max(mco, tmco)


"""
Testing:
--------
"""
input_list = [[1, 1, 0, 1, 1, 1], [1, 0, 1, 1, 0, 1]]
output_list = [3, 2]
for i in range(len(input_list)):
    assert Solution().findMaxConsecutiveOnes(input_list[i]) == output_list[i]
