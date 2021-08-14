"""
URL: https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1360/

Problem Statement:
------------------
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
    - MinStack() initializes the stack object.
    - void push(val) pushes the element val onto the stack.
    - void pop() removes the element on the top of the stack.
    - int top() gets the top element of the stack.
    - int getMin() retrieves the minimum element in the stack.

Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation:
    - MinStack minStack = new MinStack();
    - minStack.push(-2);
    - minStack.push(0);
    - minStack.push(-3);
    - minStack.getMin(); // return -3
    - minStack.pop();
    - minStack.top();    // return 0
    - minStack.getMin(); // return -2

Constraints:
-2^31 <= val <= 2^31 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(
            (val, val if self.top() is None else min(val, self.getMin()))
        )

    def pop(self) -> None:
        if self.top() is not None:
            return self.stack.pop()[0]

    def top(self) -> int:
        if self.stack == []:
            return None
        return self.stack[-1][0]

    def getMin(self) -> int:
        if self.top() is None:
            return None
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-1)
assert minStack.getMin() == -2
assert minStack.pop() == -1
assert minStack.top() == 0
assert minStack.getMin() == -2
assert minStack.pop() == 0
assert minStack.getMin() == -2
assert minStack.pop() == -2
assert minStack.getMin() is None
assert minStack.top() is None
