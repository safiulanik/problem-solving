"""
Author: Safiul Kabir [safiulanik at gmail.com]
"""

t = int(input())

for _ in range(t):
    n = int(input())
    ll = map(int, input().split())
    pos, neg = [], []
    for i in ll:
        if i >= 0:
            pos.append(i)
        else:
            neg.append(i)
    pos_sum, neg_sum = sum(pos), sum(neg) * -1
    if pos_sum == neg_sum:
        print('NO')
    else:
        print('YES')
        pos = sorted(pos, reverse=True)
        neg = sorted(neg)
        if pos_sum > neg_sum:
            print(' '.join(map(str, pos + neg)))
        else:
            print(' '.join(map(str, neg + pos)))
