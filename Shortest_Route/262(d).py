# 다익스트라 알고리즘
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]

distance = [INF] * (n + 1)

for _ in range(m):
    start, end, time = map(int, input().split())
    graph[start].append((end, time))

def dijstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijstra(c)

cnt = 0
routes = []

for r in distance:
    if r != INF and r != 0:
        cnt += 1
        routes.append(r)

print(cnt, max(routes))
