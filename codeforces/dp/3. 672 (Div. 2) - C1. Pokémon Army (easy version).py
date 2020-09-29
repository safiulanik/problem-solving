"""
URL: https://codeforces.com/problemset/problem/1420/C1
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: constructive algorithms, dp, greedy, *1300
"""

n = int(input())
for _ in range(n):
    n, q = map(int, input().split())
    array = list(map(int, input().split()))

    flip = 0
    max_strength = 0
    current = array[0]
    del array[0]
    for i in array:
        if flip == 0:
            if current > i:
                max_strength += current
                flip = 1
        else:
            if current < i:
                max_strength -= current
                flip = 0
        current = i

    if flip == 0:
        max_strength += current
    print(max_strength)
