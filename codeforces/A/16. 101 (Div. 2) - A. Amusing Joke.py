"""
URL: https://codeforces.com/problemset/problem/141/A
Author: Safiul Kabir [safiulanik at gmail.com]
"""

gn = input()
hn = input()
lp = input()

lc = [0] * 26
for l in gn:
    lc[ord(l) - 65] += 1

for l in hn:
    lc[ord(l) - 65] += 1

for l in lp:
    if lc[ord(l) - 65] == 0:
        print('NO')
        break
    else:
        lc[ord(l) - 65] -= 1
else:
    if sum(lc) == 0:
        print('YES')
    else:
        print('NO')
