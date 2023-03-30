import sys

input = sys.stdin.readline

n, m = map(int, input().split())
rices = sorted(list(map(int, input().split())))

def binary_search(arr, start, end, target):
    mid = (start + end)//2

    parts = sum([i - mid for i in arr if i - mid > 0])

    if parts >= target:
        if sum([i - mid -1 for i in arr if i - mid - 1 > 0]) < target:
            return mid
        else:
            return binary_search(arr, mid + 1, end, target)
        
    elif parts < target:
        return binary_search(arr, start, mid - 1, target)


print(binary_search(rices, 0, rices[n-1], m))