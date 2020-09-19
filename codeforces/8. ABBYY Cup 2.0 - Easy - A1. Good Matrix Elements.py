n = int(input())
mat = [[] * n] * n
for i in range(n):
    mat[i] = list(map(int, input().split()))

visited = [[False] * n for i in range(n)]
g_sum = 0
for i in range(n):
    for j in range(n):
        if i == j:
            g_sum += mat[i][j]
            visited[i][j] = True
            break

for i in range(n):
    for j in range(n):
        if i + j == n - 1 and visited[i][j] is False:
            g_sum += mat[i][j]
            visited[i][j] = True
            break

i = n // 2
for j in range(n):
    if visited[i][j] is False:
        g_sum += mat[i][j]
        visited[i][j] = True

j = n // 2
for i in range(n):
    if visited[i][j] is False:
        g_sum += mat[i][j]
        visited[i][j] = True

print(g_sum)
