"""
URL: https://codeforces.com/problemset/problem/862/A
Author: Safiul Kabir [safiulanik at gmail.com]
"""

n, x = map(int, input().split())
array = list(map(int, input().split()))

count = 0
count_array = [0] * 101
for i in array:
    count_array[i] = 1

for i in range(x + 1):
    if i == x:
        if count_array[i] == 1:
            count += 1
    elif count_array[i] == 0:
        count += 1

print(count)
