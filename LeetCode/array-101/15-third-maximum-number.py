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
        maxx = [None] * 3
        for i in range(len(nums)):
            if nums[i] not in maxx:
                for j in range(len(maxx)):
                    if maxx[j] is None:
                        maxx[j] = nums[i]
                        break
                    elif nums[i] > maxx[j]:
                        for k in range(len(maxx)-1, j, -1):
                            maxx[k] = maxx[k-1]
                        maxx[j] = nums[i]
                        break
        return maxx[0] if maxx[-1] is None else maxx[-1]


"""
Testing:
--------
"""
input_list = [
    [[3, 2, 1]],
    [[1, 2]],
    [[3, 2]],
    [[2, 2, 3, 1]],
    [[1, 2, 3, 4, 5]],
    [[5, 4, 3, 2, 1]],
]
output_list = [
    1,
    2,
    3,
    1,
    3,
    3,
]

for i in range(len(input_list)):
    result = Solution().thirdMax(*input_list[i])
    print(result, output_list[i])
    assert result == output_list[i]
