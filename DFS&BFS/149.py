import sys
input = sys.stdin.readline
cnt = 0

n, m = map(int, input().split())
ice = [list(map(int, input().rstrip())) for _ in range(n)]      # 전체 리스트를 2차원 리스트로 저장

def dfs(x, y):      # DFS를 사용하기 위해 재귀함수를 구현
    if 0 <= x < n and 0 <= y < m:
        if ice[x][y] == 0:
            ice[x][y] = 1 
            dfs(x - 1, y) 
            dfs(x + 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
            return 'ok'
        else:
            return 'No'
    else:
        return 'No' 
    
for i in range(n):
    for j in range(m):
        if dfs(i, j) == 'ok':
            cnt += 1

print(cnt)