# 해설
n, m = map(int, input().split())

nums = [int(input()) for _ in range(n)]

d = [10001]*(m + 1)
d[0] = 0

for i in range(n):
    for j in range(nums[i], m + 1):
        if d[j - nums[i]] != 10001:
            d[j] = min(d[j], d[j - nums[i]] + 1)
            print(d[j])

print(d[m])