"""
URL: https://codeforces.com/problemset/problem/1435/B
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: constructive algorithms, implementation
----------------------Verdict: TLE----------------------
"""

from sys import stdin, stdout

input, print = stdin.readline, stdout.write


def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        for __ in range(n):
            tmp = input()
        ll = []
        for i in range(m):
            ll.append(input().split())
        for i in range(n):
            for j in range(m):
                print(ll[j][i] + ' ')
            print('\n')


main()
