"""
URL: https://codeforces.com/problemset/problem/732/B
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: dp, greedy, *1000
"""

n, k = map(int, input().split())
a = list(map(int, input().split()))
min_count = 0
d = 0
for i in range(n - 1):
    if a[i] + a[i + 1] < k:
        d = k - a[i] - a[i + 1]
        min_count += d
        a[i + 1] += max(0, d)
print(min_count)

for i in range(n):
    print(a[i], end=' ')
