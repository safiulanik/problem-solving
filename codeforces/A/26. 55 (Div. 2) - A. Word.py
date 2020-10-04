"""
URL: https://codeforces.com/problemset/problem/59/A
Author: Safiul Kabir [safiulanik at gmail.com]
"""

n = input()
uc_count = 0
lc_count = 0

for c in n:
    if ord(c) > 90:
        lc_count += 1
    else:
        uc_count += 1

print(n.upper() if uc_count > lc_count else n.lower())
