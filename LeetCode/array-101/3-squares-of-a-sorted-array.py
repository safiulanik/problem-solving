"""
URL: https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3240/

Problem Statement:
------------------
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
"""
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ll = len(nums)
        left, right = 0, ll - 1
        res = []
        ml, mr = None, None
        while left < right:
            ml, mr = nums[left] ** 2, nums[right] ** 2
            if ml < mr:
                res.insert(0, mr)
                right -= 1
                mr = None
            else:
                res.insert(0, ml)
                left += 1
                ml = None
        for i in [ml, mr]:
            if i is not None:
                res.insert(0, i)
        if ll == 1:
            res.append(nums[0]**2)
        return res


"""
Testing:
--------
"""
input_list = [[-4, -1, 0, 3, 10], [-7, -3, 2, 3, 11]]
output_list = [[0, 1, 9, 16, 100], [4, 9, 9, 49, 121]]
for i in range(len(input_list)):
    assert Solution().sortedSquares(input_list[i]) == output_list[i]
