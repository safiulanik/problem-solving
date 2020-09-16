n, m = map(int, input().split())
x = [-1] * 4
y = x[:]
for i in range(n):
    tmp = list(input())
    for j in range(m):
        if tmp[j] == '*':
            for ii in range(4):
                if x[ii] == -1:
                    x[ii], y[ii] = i, j
                    break

for i in range(3):
    cx = x.count(x[i])
    if cx == 1:
        x = x[i]
        break

for i in range(3):
    cy = y.count(y[i])
    if cy == 1:
        print(x + 1, y[i] + 1)
        break
