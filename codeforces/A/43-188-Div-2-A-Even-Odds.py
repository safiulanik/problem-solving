"""
URL: https://codeforces.com/problemset/problem/318/A
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: math, *900
"""

n, k = map(int, input().split())
nn = n if n % 2 == 0 else n + 1
nn = nn // 2
if k <= nn:
    d = k * 2 - 1
else:
    d = (k - nn) * 2
print(d)
