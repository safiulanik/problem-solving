"""
URL: https://codeforces.com/problemset/problem/1422/A
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: geometry, math, *800
"""

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    print(max(a, b, c) + 1)
