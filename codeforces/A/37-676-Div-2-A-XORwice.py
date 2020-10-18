"""
URL: https://codeforces.com/problemset/problem/1421/A
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: bitmasks, math
"""

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    limit = min(a, b)
    minn = 10 ** 10
    for i in range(limit + 1):
        minn = min(minn, (a ^ i) + (b ^ i))
    print(minn)
