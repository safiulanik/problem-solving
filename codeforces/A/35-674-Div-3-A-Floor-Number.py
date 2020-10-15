"""
URL: https://codeforces.com/problemset/problem/1426/A
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: implementation, math, *800
"""

t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    count = 1
    if n <= 2:
        print(1)
    else:
        rem = (n - 2) % x
        count += (n - 2) // x
        if rem > 0:
            count += 1
        print(count)
