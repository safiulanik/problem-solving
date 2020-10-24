"""
URL: https://codeforces.com/problemset/problem/706/B
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: binary search, dp, implementation, *1000
"""

n = int(input())
x = list(map(int, input().split()))
x.sort()
q = int(input())
for _ in range(q):
    m = int(input())
    if m < x[0]:
        print(0)
    elif m >= x[-1]:
        print(n)
    else:
        count, mid, hi, lo = 0, n // 2, n, 0
        while mid < n:
            if hi < lo:
                print(len(x[:lo]))
                break
            if m == x[mid]:
                print(len(x[:mid + 1]))
                break
            elif m < x[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
            mid = (hi + lo) // 2
