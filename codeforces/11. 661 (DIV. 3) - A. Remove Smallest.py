t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    maxx = max(a)
    minn = min(a)
    tmp_list = [0] * 100  # since 1 <= ai <= 100
    for i in a:
        tmp_list[i - 1] = 1
    if sum(tmp_list[minn:maxx]) == maxx - minn:
        print('YES')
    else:
        print('NO')
