"""
URL: https://codeforces.com/problemset/problem/910/A
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: dfs and similar, dp, greedy, implementation, *800
"""

n, d = map(int, input().split())
s = input()

count = 0
i = 0
flag = False
while True:
    j = d
    while j > 0:
        if i + j < n and s[i + j] == '1':
            count += 1
            i = i + j
            if i + 1 == n:
                break
            j = d
        else:
            j -= 1
    if j == 0:
        print(-1)
        flag = True
        break
    elif i + 1 == n:
        break
    i += 1
if flag is False:
    print(count)
