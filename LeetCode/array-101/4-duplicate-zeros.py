"""
URL: https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3245/

Problem Statement:
------------------
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.

Example 1:
Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:
Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]

Note:
1 <= arr.length <= 10000
0 <= arr[i] <= 9
"""
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        ll = len(arr)
        i = 0
        while i < ll:
            if arr[i] == 0:
                arr.insert(i + 1, 0)
                del arr[-1]
                i += 1

            i += 1


"""
Testing:
--------
"""
input_list = [[1, 0, 2, 3, 0, 4, 5, 0], [1, 2, 3]]
output_list = [None, None]
for i in range(len(input_list)):
    assert Solution().duplicateZeros(input_list[i]) == output_list[i]
