"""
URL: https://leetcode.com/explore/featured/card/fun-with-arrays/523/conclusion/3270/

Problem Statement:
------------------
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:
Input: nums = [1,1]
Output: [2]

Constraints:
n == nums.length
1 <= n <= 105
1 <= nums[i] <= n

Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
"""
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ll = len(nums)
        for i in range(ll):
            while nums[nums[i] - 1] != nums[i]:
                tmp = nums[i]
                nums[i] = nums[nums[i] - 1]
                nums[tmp - 1] = tmp

        d_list = []
        for i in range(ll):
            if nums[i] != i + 1 and nums[i] == nums[nums[i] - 1]:
                d_list.append(i+1)

        return d_list


"""
Testing:
--------
"""
input_list = [
    [[4, 3, 2, 7, 8, 2, 3, 1]],
    [[1, 1]],
    [[1]],
]
output_list = [
    [5, 6],
    [2],
    []
]

for i in range(len(input_list)):
    result = Solution().findDisappearedNumbers(*input_list[i])
    print(result, output_list[i])
    assert result == output_list[i]
