"""
URL: https://codeforces.com/problemset/problem/1374/C
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: greedy, strings, *1000
"""

t = int(input())
for _ in range(t):
    move_count = 0
    n = int(input())
    s = input()
    ob_count = 0
    for i in s:
        if i == '(':
            ob_count += 1
        else:
            # i is ')'
            if ob_count > 0:
                ob_count -= 1
            else:
                move_count += 1
    print(move_count)
