n, k = map(int, input().split())
scores = list(map(int, input().split()))

if scores[k - 1] == 0:
    for i in range(k - 2, -1, -1):
        if scores[i] > 0:
            print(i + 1)
            break
    else:
        print(0)
else:
    for i in range(k, n):
        if scores[i] < scores[k - 1]:
            print(i)
            break
    else:
        print(n)
