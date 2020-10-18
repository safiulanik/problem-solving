"""
URL: https://codeforces.com/problemset/problem/1421/A
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: greedy, math
"""

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    count = 0
    for i in range(1, n):
        if a[i] <= k:
            while a[0] + a[i] <= k:
                a[i] += a[0]
                count += 1
    print(count)
