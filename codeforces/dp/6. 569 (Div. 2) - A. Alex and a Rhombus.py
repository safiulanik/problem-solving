"""
URL: https://codeforces.com/problemset/problem/1180/A
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: dp, implementation, math, *800
"""

n = int(input())
cell_count = 0
for i in range(1, n + 1):
    cell_count += 1 if i == 1 else 4 * (i - 1)

print(cell_count)
