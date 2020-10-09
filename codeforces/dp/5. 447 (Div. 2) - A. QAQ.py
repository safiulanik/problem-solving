"""
URL: https://codeforces.com/problemset/problem/894/A
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: brute force, dp, *800
"""

s = input()
count = 0
for i in range(len(s)):
    if s[i] == 'A':
        a, b = 0, 0
        for j in range(i - 1, -1, -1):
            if s[j] == 'Q':
                a += 1
        for j in range(i + 1, len(s)):
            if s[j] == 'Q':
                b += 1
        count += a * b
print(count)
