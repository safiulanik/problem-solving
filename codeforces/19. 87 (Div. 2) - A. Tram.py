"""
URL: https://codeforces.com/problemset/problem/119/A
Author: safiulanik at gmail.com
"""

n = int(input())
min_cap = 0
tmp_cap = 0
for _ in range(n):
    ex, en = map(int, input().split())
    tmp_cap = tmp_cap - ex + en
    min_cap = max(min_cap, tmp_cap)

print(min_cap)
