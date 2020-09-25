"""
URL: https://codeforces.com/problemset/problem/92/A
Author: Safiul Kabir [safiulanik at gmail.com]
"""

n, m = map(int, input().split())
summ = n * (n + 1) / 2
rem = int(m % summ)

for i in range(1, n + 1):
    if rem - i < 0:
        break
    rem -= i

print(rem)
