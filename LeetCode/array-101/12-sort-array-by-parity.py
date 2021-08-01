"""
URL: https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3260/

Problem Statement:
------------------
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

Example 1:
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
1 <= nums.length <= 5000
0 <= nums[i] <= 5000
"""
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        read_pointer, ll = 1, len(nums)
        for write_pointer in range(ll):
            if nums[write_pointer] % 2 == 1:
                while read_pointer < ll and nums[read_pointer] % 2 == 1:
                    read_pointer += 1
                if read_pointer == ll:
                    return nums
                nums[write_pointer], nums[read_pointer] = nums[read_pointer], nums[write_pointer]
            else:
                read_pointer += 1
        return nums


"""
Testing:
--------
"""
input_list = [
    [[3, 1, 2, 4]],
    [[0]],
    [[2, 4, 6, 8]],
    [[1, 3, 5, 7]],
    [[2, 3, 4, 5, 5, 7, 6, 6, 6]],
]
output_list = [
    [2, 4, 3, 1],
    [0],
    [2, 4, 6, 8],
    [1, 3, 5, 7],
    [2, 4, 6, 6, 6, 7, 3, 5, 5],
]

for i in range(len(input_list)):
    result = Solution().sortArrayByParity(*input_list[i])
    assert result == output_list[i]
