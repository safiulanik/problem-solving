"""
URL: https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1214/

Problem Statement:
------------------
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
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
    def detectCycle(self, head: ListNode) -> ListNode:
        current_node = head
        while current_node != None:
            if self.isVisitedNode(head, current_node.next, current_node):
                return current_node.next
            current_node = current_node.next
        return None

    def isVisitedNode(self, head, node, limit: ListNode) -> bool:
        if head == node or node == limit:
            return True
        current_node = head
        while current_node != limit:
            if current_node == node:
                return True
            current_node = current_node.next
        return False


"""
Testing:
--------
"""
input_list = [
    [[3, 2, 0, -4], 1],
    [[1, 2], 0],
    [[1], -1],
    [[1], 0],
    [[3, 2, 0, -4], 3],
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

    expected_output = None if input_list[i][1] == - \
        1 else nodes[input_list[i][1]]
    assert Solution().detectCycle(nodes[0]) == expected_output
