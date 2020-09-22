"""
URL: https://codeforces.com/problemset/problem/119/A
Author: safiulanik at gmail.com
"""


def gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


a, b, n = map(int, input().split())
gcd_val = gcd(a, n)
winner = 0
while gcd_val < n:
    n -= gcd_val
    if winner == 0:
        gcd_val = gcd(b, n)
        winner = 1
    else:
        gcd_val = gcd(a, n)
        winner = 0

print(winner)
