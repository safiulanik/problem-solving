"""
URL: https://codeforces.com/problemset/problem/702/A
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: dp, greedy, implementation, *800
"""

n = int(input())
array = list(map(int, input().split()))

max_inc_subarray_count = 1
tmp_count = 1
ci = array[0]
del array[0]
for i in array:
    if ci < i:
        tmp_count += 1
    else:
        max_inc_subarray_count = max(max_inc_subarray_count, tmp_count)
        tmp_count = 1
    ci = i

print(max(max_inc_subarray_count, tmp_count))
