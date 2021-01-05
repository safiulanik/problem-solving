"""
URL: https://codeforces.com/problemset/problem/451/B
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: implementation, sortings, *1300
"""


def main():
    n = int(input())
    ll = list(map(int, input().split()))

    start, end = -1, -1

    for i in range(n - 1):
        if ll[i] > ll[i + 1]:
            start = i + 1
            break

    if start == -1:
        print('yes')
        print('1 1')
        return

    for i in range(start, n - 1):
        if ll[i] < ll[i + 1]:
            end = i + 1
            break

    if start > -1 and end == -1:
        end = n

    for i in range(start - 1):
        if ll[i] > ll[end - 1]:
            print('no')
            break
    else:
        for i in range(end, n):
            if ll[i] < ll[start - 1] or (i < n - 1 and ll[i] > ll[i + 1]):
                print('no')
                break
        else:
            print('yes')
            print(f'{start} {end}')


main()
