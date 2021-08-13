"""
URL: https://leetcode.com/explore/learn/card/queue-stack/228/first-in-first-out-data-structure/1337/

Problem Statement:
------------------
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implementation the MyCircularQueue class:

    - MyCircularQueue(k) Initializes the object with the size of the queue to be k.
    - int Front() Gets the front item from the queue. If the queue is empty, return -1.
    - int Rear() Gets the last item from the queue. If the queue is empty, return -1.
    - boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
    - boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
    - boolean isEmpty() Checks whether the circular queue is empty or not.
    - boolean isFull() Checks whether the circular queue is full or not.
    - You must solve the problem without using the built-in queue data structure in your programming language. 

Example 1:
Input:
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output:
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
    - MyCircularQueue myCircularQueue = new MyCircularQueue(3);
    - myCircularQueue.enQueue(1); // return True
    - myCircularQueue.enQueue(2); // return True
    - myCircularQueue.enQueue(3); // return True
    - myCircularQueue.enQueue(4); // return False
    - myCircularQueue.Rear();     // return 3
    - myCircularQueue.isFull();   // return True
    - myCircularQueue.deQueue();  // return True
    - myCircularQueue.enQueue(4); // return True
    - myCircularQueue.Rear();     // return 4

Constraints:
1 <= k <= 1000
0 <= value <= 1000
At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.
"""
from typing import List


class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [None] * k
        self.front = -1
        self.rear = -1
        self.size = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.arr[self.rear] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.rear]

    def isEmpty(self) -> bool:
        return self.front == -1

    def isFull(self) -> bool:
        return (self.rear + 1) % self.size == self.front


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3)
assert obj.enQueue(1) is True
assert obj.enQueue(2) is True
assert obj.enQueue(3) is True
assert obj.enQueue(4) is False
assert obj.Rear() == 3
assert obj.isFull() is True
assert obj.deQueue() is True
assert obj.enQueue(4) is True
assert obj.Rear() == 4
