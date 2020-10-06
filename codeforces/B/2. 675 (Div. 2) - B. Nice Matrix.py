"""
URL: https://codeforces.com/problemset/problem/1422/B
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: greedy, implementation, *1300
"""

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    ll = list()
    for i in range(n):
        mat = list(map(int, input().split()))
        ll.append(mat)
    used = [[False for __ in range(m)] for ___ in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if used[i][j]:
                continue
            parts = list()
            oi, oj = n - 1 - i, m - 1 - j
            iis, jjs = [i, i, oi, oi], [j, oj, j, oj]
            for d in range(4):
                ni, nj = iis[d], jjs[d]
                if used[ni][nj] is False:
                    parts.append(ll[ni][nj])
                    used[ni][nj] = True
            parts = sorted(parts)
            median = parts[len(parts) // 2]
            for ii in parts:
                count += abs(ii - median)
    print(count)
