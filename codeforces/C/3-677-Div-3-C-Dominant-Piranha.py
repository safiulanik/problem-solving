"""
URL: https://codeforces.com/problemset/problem/1433/C
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: constructive algorithms, greedy
"""

t = int(input())

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    a = sorted(b, reverse=True)
    if sum(a) == len(a) * a[0]:
        print(-1)
    else:
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                if b[-1] == a[i]:
                    for j in range(n - 1, -1, -1):
                        if a[i] == b[j] and b[j] > b[j - 1]:
                            print(j + 1)
                            break
                else:
                    for j in range(n - 1):
                        if a[i] == b[j] and b[j] > b[j + 1]:
                            print(j + 1)
                            break
                break
