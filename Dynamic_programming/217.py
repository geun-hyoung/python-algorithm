arr = []

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