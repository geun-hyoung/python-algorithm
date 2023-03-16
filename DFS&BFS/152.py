import sys
from collections import deque

input = sys.stdin.readline

queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
loads = [list(map(int, input().rstrip())) for _ in range(n)]

def bfs(loads, x, y):
    while True:
        
        if 0<=x<n and 0<y<=m and loads[x][y] == 0:
            queue.append((x, y))
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>= n or ny<0 or ny>= m:
                continue
 
           
            
                     




