k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

if 1 in [k, l, m, n]:
    print(d)
else:
    count = 0
    for i in range(1, d + 1):
        for j in [k, l, m, n]:
            if i % j == 0:
                count += 1
                break
    print(count)
