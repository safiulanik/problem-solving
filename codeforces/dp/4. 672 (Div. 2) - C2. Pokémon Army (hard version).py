"""
URL: https://codeforces.com/problemset/problem/1420/C2
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: data structures, divide and conquer, dp, greedy, implementation, *2100
"""

"""This implementation is correct but gets TLE"""


def print_max_army_strength(array):
    flip = 0
    max_strength = 0
    current = array[0]
    for i in array[1:]:
        if flip == 0:
            if current > i:
                max_strength += current
                flip = 1
        else:
            if current < i:
                max_strength -= current
                flip = 0
        current = i

    if flip == 0:
        max_strength += current
    print(max_strength)


n = int(input())
for _ in range(n):
    n, q = map(int, input().split())
    array = list(map(int, input().split()))
    print_max_army_strength(array=array)
    for __ in range(q):
        index_a, index_b = map(int, input().split())
        index_a -= 1
        index_b -= 1
        array[index_a], array[index_b] = array[index_b], array[index_a]
        print_max_army_strength(array=array)
