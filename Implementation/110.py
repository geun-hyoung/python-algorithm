import sys
import collections      # Collect 라이브러리를 이용해서 전체 이동 횟수를 계산 후 한꺼번에 출력할려고 했으나 공간 밖으로 무시하는 경우가 존재

input = sys.stdin.readline

n = int(input())
moves = input().rstrip().split()
start = [1, 1]
for move in moves:
    if move == 'R':
        if start[1] == 5:
            pass
        else: 
            start[1] += 1
    elif move == 'L':
        if start[1] == 1:
            pass
        else:
            start[1] -= 1
    elif move == 'U':
        if start[0] == 1:
            pass
        else:
            start[0] -= 1
    else:
        if start[0] == 5:
            pass
        else:
            start[0] += 1

print(*start, end='')