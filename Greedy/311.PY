import sys

input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())), reverse=True)
group = 0

while True:
    try:
        cri = arr[0]
        arr = arr[cri:]
        group += 1

    except IndexError:
        break

print(group)