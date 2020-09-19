n, m = map(int, input().split())
count = 0
a = 0
while a * a <= n and a <= m:
    b = n - a * a
    if a + b * b == m:
        count += 1
    a += 1
print(count)
