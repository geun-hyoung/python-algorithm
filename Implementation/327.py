import sys

input = sys.stdin.readline

# 북동남서 > 0, 1, 2, 3
# 시작은 1

def rotate_90(now, direction):
    if direction == 'D':
        now += 1
        if now == 4 :
            now = 0
    elif direction == 'L':
        now -= 1
        if now == -1:
            now = 3
    return now


def move_snake(now, row, col, snake_tail, k, board):

    if now == 0:
        new_row = row - 1
        new_col = col

    elif now == 1:
        new_row = row
        new_col = col + 1

    elif now == 2:
        new_row = row + 1
        new_col = col

    elif now == 3:
        new_row = row
        new_col = col - 1

    try:
        if 0>new_col or  new_col >n or 0>new_row or new_row>n:
            return row, col, False, k

       
        apple = board[new_row][new_col]

        if [new_row, new_col] in snake_tail:
            print(row, col, False, k, '뱀이랑 부딪힘')
            return row, col, False, k

        if apple == 1:
            board[new_row][new_col] = 0
            snake_tail.append([new_row, new_col])
            k -= 1
            print(now, row, col, False, k, '사과가 o')
            return new_row, new_col, True, k

        else:
            print(now, row, col, False, k, '사과가 없다')
            snake_tail.append([new_row, new_col])
            del snake_tail[0]
            return new_row, new_col, True, k

    except:
        print(row, col, False, k, '보드밖으로 나감')
        return row, col, False, k


n = int(input())
k = int(input())

board = [[0 for _ in range(n)]]*n


for _ in range(k):
    x, y = map(int, input().split())
    board[x- 1][y- 1] = 1

l = int(input())

move_dict = {}

for j in range(l):
    x, y = input().split()
    move_dict[int(x)] = y

time = 1       # 초과 시간
now = 1
snake_tail = [[0,0]]
row, col = 0, 0

while True:
    try:
        dirt = move_dict[time]
        now = rotate_90(now, dirt)

    except:
        pass

    row, col, type, k = move_snake(now, row, col, snake_tail, k, board)
    time += 1

    if type == False:
        print(time)
        break
    else:
        pass