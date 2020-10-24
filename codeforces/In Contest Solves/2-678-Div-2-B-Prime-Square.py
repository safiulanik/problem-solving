"""
Author: Safiul Kabir [safiulanik at gmail.com]
"""
# a = list(map(int, input().split()))
import math


def is_prime(nn):
    if ii in prime_numbers:
        return True
    if nn == 1:
        return False
    elif nn == 2:
        prime_numbers.append(nn)
        return True
    else:
        if nn % 2 == 0:
            return False
        sqr = int(math.sqrt(nn)) + 1

        for divisor in range(3, sqr, 2):
            if nn % divisor == 0:
                return False
        prime_numbers.append(nn)
        return True


prime_numbers = []

t = int(input())
# t = 1

for _ in range(t):
    n = int(input())
    # n = 4
    if n == 2:
        print(1, 1)
        print(1, 1)
        continue
    ii = 1
    ll = []
    tmp = []
    for j in range(n):
        while is_prime(ii):
            ii += 1
        tmp.append(ii)
        if j == n - 1:
            while is_prime(sum(tmp)) is False:
                ii += 1
                while is_prime(ii):
                    ii += 1
                tmp[-1] = ii
    for i in range(n):
        ll.append(tmp.copy())

    for i in range(n):
        ii = ll[-1][i]
        while is_prime(sum([ll[ii][i] for ii in range(n)])) is False:
            ii += 1
            while is_prime(ii):
                ii += 1
            ll[-1][i] = ii

    if is_prime(sum(ll[-1])) is False:
        ii = ll[-1][-1]
        while is_prime(sum(ll[-1])) is False or is_prime(sum([ll[jj][-1] for jj in range(n)])):
            ii += 1
            if is_prime(ii):
                ii += 1
                continue
            ll[-1][-1] = ii

    for i in range(n):
        for j in range(n):
            print(ll[i][j], end=' ')
        print()
