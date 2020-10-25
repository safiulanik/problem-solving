"""
URL: https://codeforces.com/problemset/problem/617/A
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: math, *800
"""

n = int(input())
count = 0
if n > 5:
    count += n // 5
    n %= 5
if n > 0:
    count += 1
print(count)
