"""
URL: https://codeforces.com/problemset/problem/1433/BB
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: greedy, implementation
"""

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if a[i] == 1:
            break
        count -= 1
    for i in range(n - 1, -1, -1):
        if a[i] == 1:
            break
        count -= 1
    print(a.count(0) + count)
