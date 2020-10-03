"""
URL: https://codeforces.com/problemset/problem/580/A
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: brute force, dp, implementation, *900
"""

n = int(input())
a = list(map(int, input().split()))

max_range_count = 0
tmp_count = 1
last_int = a[0]
for i in range(1, n):
    if last_int <= a[i]:
        tmp_count += 1
    else:
        max_range_count = max(max_range_count, tmp_count)
        tmp_count = 1
    last_int = a[i]
max_range_count = max(max_range_count, tmp_count)
print(max_range_count)
