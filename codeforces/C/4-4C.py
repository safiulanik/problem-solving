"""
URL: https://codeforces.com/problemset/problem/4/C
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: data structures, hashing, implementation, *1300
"""


def main():
    n = int(input())
    store = dict()
    for _ in range(n):
        s = input()
        if s in store.keys():
            store[s] += 1
            print(f'{s}{store[s]}')
        else:
            store[s] = 0
            print('OK')


main()
