import sys
input = sys.stdin.readline

n, m, c = map(int, input().split())

INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 플로이드 워셜
for _ in range(m):
    start, end, time = map(int, input().split())
    graph[start][end] = time

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 모든 경우의 최단 경로를 구해주면 해당 노드에서 다른 노드까지의 최단 거리들을 더해주면 된다..?
for k in range(1, n +1):
    for a in range(1, n + 1):
        for b in range(1, n  + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

cnt = 0
routes = []

# 츨빌 노드에서 무한대 값이 아니고 0이 아닌 값은 해당 노드로 가는데 최소 시간을 알려주니까 해당 cnt를 세고 그 중 가장 시간이 
# 많이 소요되는 시간이 총 소요시간
for city in graph[c]:
    if city != INF and city != 0:
        cnt += 1
        routes.append(city)

print(cnt, max(routes))