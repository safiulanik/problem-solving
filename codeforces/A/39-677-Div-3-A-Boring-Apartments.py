"""
URL: https://codeforces.com/problemset/problem/1433/A
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: implementation, math
"""

t = int(input())

for _ in range(t):
    n = input()
    count = 10 * (int(n[0]) - 1)
    ll = len(n)
    for i in range(1, ll + 1):
        count += i
    print(count)
