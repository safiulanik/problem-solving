"""
URL: https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3247/

Problem Statement:
------------------
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:
The judge will test your solution with the following code:
-----------------------------------------------------------------------
int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
-----------------------------------------------------------------------
If all assertions pass, then your solution will be accepted.

Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).

Constraints:
0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length, i = 0, 0
        ll = len(nums)
        while i < ll:
            if nums[i] == val:
                del nums[i]
                ll -= 1
            else:
                length += 1
                i += 1
        return length


"""
Testing:
--------
"""
input_list = [
    [[3, 2, 2, 3], 3],
    [[0, 1, 2, 2, 3, 0, 4, 2], 2]
]
output_list = [2, 5]

for i in range(len(input_list)):
    assert Solution().removeElement(*input_list[i]) == output_list[i]
    """
    The problem requires to also check the elements of the nums list
    But this is not needed for this solution as I've entierly deleted the element
    from the list instead of using a length var to track the next insertion position.

    This check might be required for some other solution(s).
    """
