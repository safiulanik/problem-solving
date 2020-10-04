"""
URL: https://codeforces.com/problemset/problem/136/A
Author: Safiul Kabir [safiulanik at gmail.com]
"""

n = int(input())
inp = list(map(int, input().split()))
outp = [0] * n
for i in range(n):
    outp[inp[i] - 1] = i + 1

print(' '.join(map(str, outp)))
