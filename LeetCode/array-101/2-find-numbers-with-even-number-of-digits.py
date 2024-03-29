"""
URL: https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3237/

Problem Statement:
------------------
Given an array nums of integers, return how many of them contain an even number of digits.

Example 1:
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.

Example 2:
Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.

Constraints:
1 <= nums.length <= 500
1 <= nums[i] <= 10^5
"""
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for n in nums:
            if len(str(n)) % 2 == 0:
                count += 1
        return count


"""
Testing:
--------
"""
input_list = [[12, 345, 2, 6, 7896], [555, 901, 482, 1771]]
output_list = [2, 1]
for i in range(len(input_list)):
    assert Solution().findNumbers(input_list[i]) == output_list[i]
