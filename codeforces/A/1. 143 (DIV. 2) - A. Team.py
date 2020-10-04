t = int(input())
count = 0
for _ in range(t):
    inp_sum = sum(list(map(int, input().split())))
    if inp_sum >= 2:
        count += 1
print(count)
