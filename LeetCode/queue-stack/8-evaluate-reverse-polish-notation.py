"""
URL: https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1394/

Problem Statement:
------------------
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Ref: http://en.wikipedia.org/wiki/Reverse_Polish_notation

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
 

Constraints:
1 <= tokens.length <= 10^4
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                b, a = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(a+b)
                elif token == "-":
                    stack.append(a-b)
                elif token == "*":
                    stack.append(a*b)
                elif token == "/":
                    stack.append(int(a/b))
            else:
                stack.append(int(token))
        return stack.pop()


"""
Testing:
--------
"""
input_list = [
    [["2", "1", "+", "3", "*"]],
    [["4", "13", "5", "/", "+"]],
    [["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]],
]
output_list = [
    9,
    6,
    22,
]

for i in range(len(input_list)):
    result = Solution().evalRPN(*input_list[i])
    print(result, output_list[i])
    assert result == output_list[i]
