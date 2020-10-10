"""
URL: https://codeforces.com/problemset/problem/1206/B
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: dp, implementation, *900
"""

n = int(input())
a = map(int, input().split())

move_count, count_gtz, count_ltz, count_zero = 0, 0, 0, 0
for i in a:
    if i == 0:
        count_zero += 1
    elif i > 0:
        count_gtz += 1
        move_count += i - 1
    else:
        count_ltz += 1
        move_count += abs(i - -1)

if count_ltz % 2 == 0:
    move_count += count_zero
else:
    if count_zero > 0:
        move_count += count_zero
    else:
        move_count += 2

print(move_count)
