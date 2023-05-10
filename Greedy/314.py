n = int(input())

nums = list(map(int, input().split()))
nums.sort()

arr = [i for i in range(n + 1)]
new_arr = []

for i in range(n):
    for j in range(n):

        try:
            temp_result = sum(nums[j:j + i + 1])
            new_arr.append(temp_result)
        except IndexError:
            pass

new_arr = list(set(new_arr))

for j in range(1, new_arr[-1] + 1):
    if j != new_arr[j - 1]:
        print(j)
        break
    else:
        pass
    if j == new_arr[-1]:
        print(new_arr[-1] + 1)