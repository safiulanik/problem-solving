"""
URL: https://codeforces.com/problemset/problem/144/A
Author: Safiul Kabir [safiulanik at gmail.com]
"""

n = int(input())
mil = list(map(int, input().split()))

count = 0

maxx_index = mil.index(max(mil))
while maxx_index - 1 >= 0:
    mil[maxx_index - 1], mil[maxx_index] = mil[maxx_index], mil[maxx_index - 1]
    count += 1
    maxx_index -= 1

mil = mil[::-1]
minn_index = mil.index(min(mil))
while minn_index - 1 >= 0:
    mil[minn_index - 1], mil[minn_index] = mil[minn_index], mil[minn_index - 1]
    count += 1
    minn_index -= 1

print(count)
