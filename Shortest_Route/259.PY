# 플로이도 워셜 소스 코드 활용
import sys
input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

routes = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b], graph[b][a] = 1, 1

x, k = map(int, input().split())

for k in range(1, n +1):
    for a in range(1, n + 1):
        for b in range(1, n  + 1):
            graph[a][b] = min(graph[a][b], graph[k] + graph[k][b])


if graph[1][k] + graph[k][x] != INF:
    print(graph[1][k] + graph[k][x])
else:
    print(-1)