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
