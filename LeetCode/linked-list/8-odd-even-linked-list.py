"""
URL: https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1208/

Problem Statement:
------------------
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

Constraints:
n == number of nodes in the linked list
0 <= n <= 10^4
-10^6 <= Node.val <= 10^6
"""
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        odd = head
        even = head.next
        even_start = head.next
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next

            even.next = even.next.next
            even = even.next

        odd.next = even_start
        return head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
Solution().oddEvenList(head=head)
while head is not None:
    print(head.val, end=', ')
    head = head.next

"""
1 2 3 4 5
1 3 4 5
2 4 5
1 3 2 4 5

1 3 2 4 5
1 3 5 2 4

2 1 3 5 6 4 7
2 3 1 5 6 4 7
2 3 6 1 5 4 7
2 3 6 7 1 5 4
"""
