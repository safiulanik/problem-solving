"""
URL: https://codeforces.com/problemset/problem/894/A
Author: Safiul Kabir [safiulanik at gmail.com]
Tags: brute force, dp, *800
"""


def count_QAQ(s, count):
    for i in range(len(s) - 2):
        if s[i] == 'Q':
            if s[i + 1] != 'A':
                count_QAQ(f'Q{s[i + 2:]}', count)
            else:
                # if s[i+2] != 'Q':
                if s[i + 2] == 'Q':
                    count += 1
                count_QAQ(f'QA{s[i + 3:]}', count)
    return count


s = input()
count = 0
tmp_s = ''
for c in s:
    if c in 'QA':
        tmp_s += c
s = tmp_s

print(count_QAQ(s, count))
