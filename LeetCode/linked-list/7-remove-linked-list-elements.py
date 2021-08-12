"""
URL: https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1207/

Problem Statement:
------------------
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:
Input: head = [], val = 1
Output: []

Example 3:
Input: head = [7,7,7,7], val = 7
Output: []

Constraints:
The number of nodes in the list is in the range [0, 104].
1 <= Node.val <= 50
0 <= val <= 50
"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        """Approach 1: Creating new ListNode"""
        # if head is None:
        #     return head
        # node = ListNode(-1)
        # itt = node
        # while head is not None:
        #     if head.val != val:
        #         itt.next = ListNode(head.val)
        #         itt = itt.next
        #     head = head.next
        # return node.next

        """Approach 2: Updating existing Linked List"""
        node = ListNode(-1)
        node.next = head
        head = node
        while head and head.next:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        return node.next


head = ListNode(1)
head.next = ListNode(6)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(6)
# head.next.next.next.next = ListNode(5)
Solution().removeElements(head=head, val=6)
