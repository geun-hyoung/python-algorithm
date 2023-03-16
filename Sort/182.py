import sys
input = sys.stdin.readline

n, k = map(int, input().split())

a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)

cnt = 0

for i, j in zip(a, b):
    if cnt == k:
        print(sum(a))
        break
    if i < j:   
        a[cnt] = b[cnt]
        
    cnt += 1
