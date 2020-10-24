"""
URL: https://codeforces.com/problemset/problem/753/A
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: dp, greedy, math, *1000
"""

n = int(input())
count = 0
a = []
summ = 0
for i in range(1, n + 1):
    summ += i
    if summ > n:
        break
    count += 1
    a.append(i)
if summ > n:
    a[-1] += n - summ + i
print(count)
print(' '.join(map(str, a)))
