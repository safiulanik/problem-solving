"""
URL: https://codeforces.com/problemset/problem/1426/A
Author: Safiul Kabir [safiulanik at gmail.com]
Tags:
"""

t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    count = 1
    if n <= 2:
        print(1)
    else:
        for i in range(3, n + 1, x):
            count += 1
        print(count)
