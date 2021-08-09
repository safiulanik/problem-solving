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
