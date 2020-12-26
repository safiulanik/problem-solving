"""
URL: https://codeforces.com/problemset/problem/459/B
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: combinatorics, implementation, sortings, *1300
"""


def main():
    n = int(input())
    ll = sorted(map(int, input().split()))
    if ll[0] == ll[-1]:
        ncr = n * (n - 1)
        ncr //= 2
        print(f'0 {ncr}')
    else:
        minn = ll[0]
        min_count = 1
        for i in range(1, n):
            if minn == ll[i]:
                min_count += 1
            else:
                break
        maxx = ll[-1]
        max_count = 1
        for i in range(n - 2, 0, -1):
            if maxx == ll[i]:
                max_count += 1
            else:
                break
        print(f'{maxx - minn} {min_count * max_count}')


main()
