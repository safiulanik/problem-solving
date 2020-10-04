"""
URL: https://codeforces.com/problemset/problem/104/A
Author: Safiul Kabir [safiulanik at gmail.com]
"""

deck = [i for i in range(1, 12)] * 4 + [10, 10, 10] * 4
deck.remove(10)  # removing the queen of spade
n = int(input()) - 10
print(deck.count(n))
