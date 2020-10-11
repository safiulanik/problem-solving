"""
URL: https://codeforces.com/problemset/problem/1113/A
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: dp, greedy, math, *900
"""

n, v = map(int, input().split())
if n - 1 <= v:
    print(n - 1)
else:
    minn = v
    for i in range(2, n - v + 1):
        minn += i
    print(minn)
