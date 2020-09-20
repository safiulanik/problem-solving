n = int(input())
ln = input()

tmp_str = ln
if len(tmp_str.replace('4', '').replace('7', '')) > 0:
    print('NO')
else:
    sum_1 = sum(map(int, list(ln[:n // 2])))
    sum_2 = sum(map(int, list(ln[n // 2:])))
    if sum_1 == sum_2:
        print('YES')
    else:
        print('NO')
