"""
URL: https://codeforces.com/problemset/problem/1422/C
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: combinatorics, dp, math, *1700
---------------------In Progress---------------------
"""

mod = 10 ** 9 + 7


def a(s):
    # s = input()
    ll = len(s)

    summ = 0
    for i in range(ll):
        current_digit = int(s[i])
        c1 = current_digit * 10 ** (ll - i - 1) * i * (i + 1) // 2
        c2_coff = ''.join([str(j) for j in range(ll - i - 1, 0, -1)])
        if len(c2_coff) > 9:
            c2_coff = 987654321
        elif len(c2_coff) > 0:
            c2_coff = int(c2_coff)
        else:
            c2_coff = 0
        c2 = current_digit * c2_coff

        summ += c1
        summ += c2
        summ %= mod
    print(summ)


a('100500100500')
a('107')
