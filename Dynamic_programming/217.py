arr = []

# 전체 경우르 파악함 -> 효율적이지 못하다.
def make_one(x, cnt, arr):
    y = cnt

    if x == 1:
        arr.append(y)
        return arr
    
    nums = []
    if x%5 == 0:
        nums.append(x//5)
    if x%3 == 0:
        nums.append(x//3)
    if x%2 == 0:
        nums.append(x//2)
    nums.append(x-1)

    for x in nums:
        make_one(x, y + 1, arr) 

make_one(int(input()), 0, arr)
print(min(arr))

# 답안
# 보텀업 다이나믹 프로그래밍을 떠올려야한다. 상향식, 기초적인 문제
x = int(input())
 
d = [0] * 30001

for i in range(2, x + 1):
    d[i] = d[i - 1] + 1

    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)

print(d[x])