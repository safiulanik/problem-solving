"""
URL: https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1209/

Problem Statement:
------------------
Given the head of a singly linked list, return true if it is a palindrome.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

Constraints:
The number of nodes in the list is in the range [1, 10^5].
0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
"""
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            if fast and fast.next:
                # reverse current slow node
                old_head = head
                head = slow.next
                slow.next = slow.next.next
                head.next = old_head
            else:
                slow = slow.next

        if fast:
            slow = slow.next

        while head and slow:
            if head.val != slow.val:
                return False
            head, slow = head.next, slow.next

        return True


"""
Testing:
--------
"""
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(1)
assert Solution().isPalindrome(head=head) == True
while head is not None:
    print(head.val, end=', ')
    head = head.next
