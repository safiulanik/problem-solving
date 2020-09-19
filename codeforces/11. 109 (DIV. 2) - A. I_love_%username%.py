n = int(input())
performance = list(map(int, input().split()))

lo_pivot = hi_pivot = performance[0]
count = 0
for i in range(1, n):
    if performance[i] > hi_pivot:
        count += 1
        hi_pivot = performance[i]
    elif performance[i] < lo_pivot:
        count += 1
        lo_pivot = performance[i]

print(count)
