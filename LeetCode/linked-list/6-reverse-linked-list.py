"""
URL: https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1205/

Problem Statement:
------------------
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode, node: ListNode = None) -> ListNode:
        """Approach 1: Using loop"""
        # if head is None:
        #     return head
        # node = head
        # while node.next is not None:
        #     old_head = head
        #     head = node.next
        #     node.next = node.next.next
        #     head.next = old_head
        # return head

        """Approach 2: Using pythonic loop"""
        # cur, prev = head, None
        # while cur is not None:
        #     cur.next, cur, prev = prev, cur.next, cur
        # return prev

        """Approach 3: Using recursion"""
        if head is None:
            return head
        if node is None:
            node = head
        if node.next is None:
            return head
        old_head = head
        head = node.next
        node.next = node.next.next
        head.next = old_head
        return self.reverseList(head, node)


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
Solution().reverseList(head=head)
