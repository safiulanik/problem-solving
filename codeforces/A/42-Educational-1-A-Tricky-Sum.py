"""
URL: https://codeforces.com/problemset/problem/598/A
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: math, *900
"""

t = int(input())
for _ in range(t):
    n = int(input())
    s_all = n * (n + 1) // 2
    s_pow = 0
    i = 1
    while i < n + 1:
        s_pow += i
        i *= 2
    s_pow *= 2
    print(s_all - s_pow)
