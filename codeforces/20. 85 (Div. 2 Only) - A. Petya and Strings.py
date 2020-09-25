"""
URL: https://codeforces.com/problemset/problem/112/A
Author: Safiul Kabir [safiulanik at gmail.com]
"""

s1 = input().lower()
s2 = input().lower()
if s1 == s2:
    print(0)
elif s1 < s2:
    print(-1)
else:
    print(1)
