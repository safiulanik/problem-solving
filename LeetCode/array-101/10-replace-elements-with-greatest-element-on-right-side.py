"""
URL: https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/

Problem Statement:
------------------
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

Example 1:
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation: 
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.

Example 2:
Input: arr = [400]
Output: [-1]
Explanation: There are no elements to the right of index 0.
 

Constraints:
1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5
"""
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ll = len(arr)
        for i in range(ll):
            if i == ll-1:
                arr[i] = -1
                break
            maxx = arr[i+1]
            for j in range(i+2, ll):
                if arr[j] > maxx:
                    maxx = arr[j]
            arr[i] = maxx
        return arr


"""
Testing:
--------
"""
input_list = [
    [[17, 18, 5, 4, 6, 1]],
    [[400]],
]
output_list = [
    [18, 6, 6, 6, 1, -1],
    [-1],
]

for i in range(len(input_list)):
    assert Solution().replaceElements(*input_list[i]) == output_list[i]
