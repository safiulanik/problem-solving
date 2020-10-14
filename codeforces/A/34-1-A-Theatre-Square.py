"""
URL: https://codeforces.com/problemset/problem/1/A
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: math, *1000
"""

n, m, a = map(int, input().split())
n = n // a + (1 if n % a > 0 else 0)
m = m // a + (1 if m % a > 0 else 0)
print(n * m)
