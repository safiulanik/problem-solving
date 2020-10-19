"""
URL: https://codeforces.com/problemset/problem/1182/A
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: math, dp, *1000
"""

n = int(input())
if n % 2 == 1:
    print(0)
else:
    ways = 2 ** (n // 2)
    print(ways)
