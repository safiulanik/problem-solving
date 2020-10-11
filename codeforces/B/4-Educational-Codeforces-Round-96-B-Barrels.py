"""
URL: https://codeforces.com/problemset/problem/1430/B
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: greedy, implementation, sortings
"""

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    ll = sorted(list(map(int, input().split())))
    if sum(ll) == 0 or len(ll) == 1:
        print(0)
    else:
        for i in range(n - 2, -1, -1):
            if k == 0:
                break
            ll[-1] += ll[i]
            k -= 1
        print(ll[-1])
