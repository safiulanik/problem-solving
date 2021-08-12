"""
URL: https://leetcode.com/explore/learn/card/linked-list/209/singly-linked-list/1290/

Problem Statement:
------------------
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.

A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.

If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:
    - MyLinkedList() Initializes the MyLinkedList object.
    - int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
    - void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
    - void addAtTail(int val) Append a node of value val as the last element of the linked list.
    - void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
    - void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
"""


class Node:

    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if self.head is None:
            return -1
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
            if current_node is None:
                return -1
        return current_node.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)
        node.next = self.head
        self.head = node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        current_node = self.head
        if current_node is None:
            self.addAtHead(val)
            return
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
            return
        node = Node(val)
        current_node = self.head
        for i in range(index-1):
            current_node = current_node.next
            if current_node is None:
                return
        node.next = current_node.next
        current_node.next = node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0:
            self.head = self.head.next if self.head else None
            return
        current_node = self.head
        for i in range(index-1):
            current_node = current_node.next
            if current_node is None:
                return -1
        current_node.next = current_node.next.next if current_node.next is not None else None

    def printLinkedList(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.val, end=' ')
            current_node = current_node.next
        print()


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(2)
obj.printLinkedList()
obj.addAtIndex(0, 1)
obj.printLinkedList()
print(obj.get(1))
