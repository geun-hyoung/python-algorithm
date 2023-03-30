import sys

input = sys.stdin.readline

n = int(input())
n_numbers = sorted(list(map(int, input().split())))

m = int(input())
m_numbers = sorted(list(map(int, input().split())))


def binary_search(arr, start, end, target):
    mid = (start + end) // 2
    print(start, end)
    if start > end:
        return 'no'

    if arr[mid] == target:
        return 'yes'

    elif arr[mid] > target:
        return binary_search(n_numbers, start, mid - 1, target)

    else:
        return binary_search(n_numbers, mid + 1, end, target)


for i in m_numbers:
    print(binary_search(n_numbers, 0, n - 1, i))