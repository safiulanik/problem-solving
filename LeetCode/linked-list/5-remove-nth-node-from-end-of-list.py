"""
URL: https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1296/

Problem Statement:
------------------
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

Follow up: Could you do this in one pass?
"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first = second = ListNode()
        first.next = head
        for i in range(n + 1):
            first = first.next
        if first is None:
            return head.next
        while first is not None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return head
