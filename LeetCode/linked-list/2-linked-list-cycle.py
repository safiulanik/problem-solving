"""
URL: https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1212/

Problem Statement:
------------------
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Constraints:
The number of the nodes in the list is in the range [0, 10^4].
-10^5 <= Node.val <= 10^5
pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        pointer1, pointer2 = head, head
        while pointer2 is not None:
            if pointer2.next is not None:
                pointer2 = pointer2.next.next
                pointer1 = pointer1.next
                if pointer1 == pointer2:
                    return True
            else:
                pointer2 = pointer2.next
        return False


"""
Testing:
--------
"""
input_list = [
    [[3, 2, 0, -4], 1],
    [[1, 2], 0],
    [[1], -1],
]
output_list = [
    True,
    True,
    False,
]

for i in range(len(input_list)):
    nodes = []
    nodes.append(ListNode(input_list[i][0][0]))
    current_node = nodes[0]
    for j in range(1, len(input_list[i][0])):
        node = ListNode(input_list[i][0][j])
        nodes.append(node)
        current_node.next = node
        current_node = node

    if input_list[i][1] != -1:
        current_node.next = nodes[input_list[i][1]]

    assert Solution().hasCycle(nodes[0]) == output_list[i]
