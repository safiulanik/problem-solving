"""
URL: https://www.hackerrank.com/challenges/balanced-brackets/
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: data structure, stack
"""


def is_balanced(s):
    forward_stack = []
    for c in s:
        for symbol_couple in [('(', ')'), ('{', '}'), ('[', ']')]:
            if c == symbol_couple[0]:
                forward_stack.append(symbol_couple[0])
            elif c == symbol_couple[1]:
                try:
                    if forward_stack.pop() != symbol_couple[0]:
                        return "NO"
                except:
                    return "NO"
    if len(forward_stack) == 0:
        return "YES"
    return "NO"


assert is_balanced("{[()]}") == "YES"
assert is_balanced("{[(])}") == "NO"
assert is_balanced("{{[[(())]]}}") == "YES"
assert is_balanced("{(([])[])[]}") == "YES"
