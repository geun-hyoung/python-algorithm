# 점화식을 생각하면, 점화식 = max(a(i -1), a(i - 2) + k)
# 왜냐하면 문제 조건 중에 바로 옆칸만 지나지 않으면 되기 때문에 현재칸과 한칸 떨어진칸 vs 바로 옆칸을 비교해서 값을 저장하고 진행 하면됨 
import sys
input = sys.stdin.readline

n = int(input())
k = list(map(int, input().split()))

d = [0] * 100

d[0] = k[0]
d[1] = max(k[0], k[1])
for i in range(2, n):
    d[i] = max(d[i -1], d[i - 2] + k[i])

print(d[n - 1])


