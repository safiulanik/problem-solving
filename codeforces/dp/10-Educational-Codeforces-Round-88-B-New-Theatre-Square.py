"""
URL: https://codeforces.com/problemset/problem/1359/B
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: brute force, dp, greedy, implementation, two pointers, *1000
"""

t = int(input())

for _ in range(t):
    n, m, x, y = map(int, input().split())
    count = 0
    for __ in range(n):
        a = list(input())
        for i in range(m):
            if a[i] == '.':
                if y > 2 * x:
                    count += x
                else:
                    if i < m - 1:
                        if a[i + 1] == '.':
                            count += y
                            a[i + 1] = '*'
                        else:
                            count += x
                    else:
                        count += x
    print(count)
