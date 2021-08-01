"""
URL: https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/

Problem Statement:
------------------
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:
    - arr.length >= 3
    - There exists some i with 0 < i < arr.length - 1 such that:
        - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
        - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:
Input: arr = [2,1]
Output: false

Example 2:
Input: arr = [3,5,5]
Output: false

Example 3:
Input: arr = [0,3,2,1]
Output: true
 

Constraints:
1 <= arr.length <= 10^4
0 <= arr[i] <= 10^4
"""
from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        increasing = True
        for i in range(1, len(arr)):
            if arr[i-1] == arr[i]:
                return False
            if increasing:
                if arr[i-1] > arr[i]:
                    if i == 1:
                        return False
                    increasing = False
            else:
                if arr[i-1] < arr[i]:
                    return False
        if increasing is True:
            return False
        return True


"""
Testing:
--------
"""
input_list = [
    [[2, 1]],
    [[3, 5, 5]],
    [[0, 3, 2, 1]],
    [[2, 0, 2]],
    [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
]
output_list = [
    False,
    False,
    True,
    False,
    False,
]

for i in range(len(input_list)):
    assert Solution().validMountainArray(*input_list[i]) == output_list[i]
