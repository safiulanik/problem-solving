"""
URL: https://codeforces.com/problemset/problem/1453/A
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: implementation, *800
"""


def main():
    t = int(input())

    for _ in range(t):
        n, m = map(int, input().split())
        nl = list(map(int, input().split()))
        ml = list(map(int, input().split()))
        count = 0
        i, j = 0, 0
        while i < n and j < m:
            if nl[i] == ml[j]:
                count += 1
                i += 1
                j += 1
            elif nl[i] > ml[j]:
                j += 1
            else:
                i += 1
        print(count)


main()
