"""
URL: https://codeforces.com/problemset/problem/1323/A
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: brute force, dp, greedy, implementation, *800
"""

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    flag = False
    odd_count = 0
    odd_index = -1
    for i in range(n):
        if a[i] % 2 == 0:
            print(1)
            print(i + 1)
            flag = True
            break
        else:
            odd_count += 1
            if odd_count == 2:
                print(2)
                print(odd_index, i + 1)
                flag = True
                break
            odd_index = i + 1
    if not flag:
        print("-1")
