"""
URL: https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3157/

Problem Statement:
------------------
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1

Follow up: Could you minimize the total number of operations done?
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        read_pointer = 1
        ll = len(nums)
        for write_pointer in range(ll):
            if nums[write_pointer] == 0:
                while read_pointer < ll and nums[read_pointer] == 0:
                    read_pointer += 1
                if read_pointer == ll:
                    break
                nums[write_pointer] = nums[read_pointer]
                nums[read_pointer] = 0
            else:
                read_pointer += 1


"""
Testing:
--------
"""
input_list = [
    [[0, 1, 0, 3, 12]],
    [[0, 0]],
    [[0]],
    [[2, 1]],
    [[4, 2, 4, 0, 0, 3, 0, 5, 1, 0]],
]
output_list = [
    [1, 3, 12, 0, 0],
    [0, 0],
    [0],
    [2, 1],
    [4, 2, 4, 3, 5, 1, 0, 0, 0, 0],
]

for i in range(len(input_list)):
    Solution().moveZeroes(*input_list[i])
    assert input_list[i][0] == output_list[i]
