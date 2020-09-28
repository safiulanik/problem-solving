"""
URL: https://codeforces.com/problemset/problem/996/A
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: dp, greedy, *800
"""

bills = [100, 20, 10, 5, 1]
n = int(input())

count = 0
while n > 0:
    for bill in bills:
        if n >= bill:
            count += n // bill
            n %= bill
print(count)
