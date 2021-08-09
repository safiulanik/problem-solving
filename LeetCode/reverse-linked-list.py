# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode, node: ListNode = None) -> ListNode:
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
