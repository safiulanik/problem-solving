"""
URL: https://codeforces.com/problemset/problem/1421/A
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: bitmasks, math
"""

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    print(a ^ b)
