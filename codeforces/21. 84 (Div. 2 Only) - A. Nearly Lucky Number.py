"""
URL: https://codeforces.com/problemset/problem/110/A
Author: Safiul Kabir [safiulanik at gmail.com]
"""

n = input()
count = 0
for c in n:
    if c in ['4', '7']:
        count += 1

count = str(count)
for c in count:
    if c not in ['4', '7']:
        print("NO")
        break
else:
    print("YES")
