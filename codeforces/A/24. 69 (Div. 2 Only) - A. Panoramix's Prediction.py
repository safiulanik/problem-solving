"""
URL: https://codeforces.com/problemset/problem/80/A
Author: Safiul Kabir [safiulanik at gmail.com]
"""
from math import sqrt

n, m = map(int, input().split())


def isprime(nn):
    if nn % 2 == 0:
        return False
    for i in range(3, int(sqrt(nn)) + 1):
        if nn % i == 0:
            return False
    return True


for i in range(n + 1, m + 1):
    if isprime(i):
        if i == m:
            print("YES")
        else:
            print("NO")
        break
else:
    print("NO")
