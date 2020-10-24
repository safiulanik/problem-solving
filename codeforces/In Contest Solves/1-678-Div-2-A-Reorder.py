"""
URL: https://codeforces.com/contest/1436/problem/A
Author: Safiul Kabir [safiulanik at gmail.com]
"""

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    if sum(a) == m:
        print('YES')
    else:
        print('NO')
