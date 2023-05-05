nums =list(map(int, list(input())))
result = 0

for n in nums:
    if result+n > result*n:     result += n

    else:       result = result*n

print(result)