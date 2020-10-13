"""
URL: https://codeforces.com/problemset/problem/1430/A
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: brute force, constructive algorithms, math
"""

t = int(input())

possible = [False for i in range(1010)]
possible[0] = True
for i in range(1000):
    if possible[i] is False:
        continue
    else:
        possible[i + 3] = possible[i + 5] = possible[i + 7] = True

for _ in range(t):
    n = int(input())
    if possible[n]:
        counts = [0, 0, 0]
        while n != 0:
            if possible[n - 3]:
                counts[0] += 1
                n -= 3
            elif possible[n - 5]:
                counts[1] += 1
                n -= 5
            else:
                counts[2] += 1
                n -= 7
        print(' '.join(map(str, counts)))
    else:
        print(-1)
