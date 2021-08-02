"""
URL: https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3231/

Problem Statement:
------------------
Given integer array nums, return the third maximum number in this array. If the third maximum does not exist, return the maximum number.

Example 1:
Input: nums = [3,2,1]
Output: 1
Explanation: The third maximum is 1.

Example 2:
Input: nums = [1,2]
Output: 2
Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

Example 3:
Input: nums = [2,2,3,1]
Output: 1
Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.

Constraints:
1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1

Follow up: Can you find an O(n) solution?
"""
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maxx = [nums[0]]
        ll = len(nums)
        for i in range(1, ll):
            if nums[i] not in maxx:
                for j in range(len(maxx) - 1, -1, -1):
                    if maxx[j] < nums[i]:
                        if len(maxx) < 3:
                            maxx.append(nums[i])
                        else:
                            for k in range(j-1, -1, -1):
                                maxx[k] = maxx[k+1]
                            maxx[j] = nums[i]
        print(nums, maxx)
        return maxx[0]


"""
Testing:
--------
"""
input_list = [
    [[3, 2, 1]],
    [[1, 2]],
    [[2, 2, 3, 1]],
]
output_list = [
    1,
    2,
    1,
]

for i in range(len(input_list)):
    assert Solution().thirdMax(*input_list[i]) == output_list[i]
