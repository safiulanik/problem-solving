"""
URL: https://codeforces.com/problemset/problem/546/A
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: brute force, implementation, math, *800
"""

k, n, w = map(int, input().split())
required = k * w * (w + 1) // 2
required -= n
if required < 0:
    print(0)
else:
    print(required)
