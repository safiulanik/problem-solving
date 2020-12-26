"""
URL: https://codeforces.com/problemset/problem/706/B
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: binary search, dp, implementation, *1100
"""
from sys import stdin, stdout

input = stdin.readline


def main():
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    q = int(input())
    dp = {}
    for _ in range(q):
        m = int(input())
        if m in dp.keys():
            print(dp[m])
            continue
        if m < x[0]:
            print(0)
            dp[m] = 0
        elif m >= x[-1]:
            print(n)
            dp[m] = n
        else:
            count, mid, hi, lo = 0, n // 2, n, 0
            while mid < n:
                if hi < lo:
                    ans = len(x[:lo])
                    print(ans)
                    dp[m] = ans
                    break
                if m == x[mid]:
                    for i in range(mid + 1, n):
                        if m == x[i]:
                            mid += 1
                        else:
                            break
                    ans = len(x[:mid + 1])
                    dp[m] = ans
                    print(ans)
                    break
                elif m < x[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
                mid = (hi + lo) // 2


main()
