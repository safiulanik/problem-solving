"""
URL: https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1361/

Problem Statement:
------------------
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true

Constraints:
1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.
"""


class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            for pair in [('(', ')'), ('{', '}'), ('[', ']')]:
                if i == pair[0]:
                    stack.append(i)
                elif i == pair[1]:
                    if not stack:
                        return False
                    elif stack.pop() == pair[0]:
                        break
                    else:
                        return False

        return not stack


"""
Testing:
--------
"""
input_list = [
    ["()"],
    ["()[]{}"],
    ["(]"],
    ["([)]"],
    ["{[]}"]
]
output_list = [
    True,
    True,
    False,
    False,
    True,
]

for i in range(len(input_list)):
    result = Solution().isValid(*input_list[i])
    print(result, output_list[i])
    assert result == output_list[i]
