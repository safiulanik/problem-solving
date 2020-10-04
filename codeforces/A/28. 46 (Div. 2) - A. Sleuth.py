"""
URL: https://codeforces.com/problemset/problem/49/A
Author: Safiul Kabir [safiulanik at gmail.com]
"""

s = ''.join(input().split()).lower()
if s[-2] in ['a', 'e', 'i', 'o', 'u', 'y']:
    print('YES')
else:
    print('NO')
