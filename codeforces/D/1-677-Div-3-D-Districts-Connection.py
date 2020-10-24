"""
URL: https://codeforces.com/problemset/problem/1433/D
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: constructive algorithms, dfs and similar, dsu, trees
"""

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    visited = [False for _ in range(n)]
    possible = False
    for i in range(1, n):
        if a[i] != a[0]:
            possible = True
    if not possible:
        print('NO')
    else:
        print('YES')
        for i in range(n - 1):
            for j in range(i + 1, n):
                if a[i] != a[j] and (visited[i] is False or visited[j] is False):
                    visited[i] = visited[j] = True
                    print(i + 1, j + 1)
