import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a, b, d = map(int, input().split())

old_point = []      # 좌표 이동을 저장하기 위한 List
board = [list(map(int, input().split())) for _ in range(n)]     # 전체 맵의 형식을 받아서 바다와 육지를 구분한다.
cnt = 0
old_point.append([a, b])      # 초기 좌표를 넣어준다.

def move(a, b, d, cnt):     # 처음 좌표의 방향을 바꿈과 동시에 해당 방향으로 이동이 가능하면 이동시키는 함수
    x, y = a, b

    if d == 0:
        d = 3
        y -= 1
    elif d == 1:
        d = 0
        x -= 1
    elif d == 2:
        d = 1
        y += 1
    else:
        d = 2
        x += 1

    point = [x, y]  # 방향을 왼쪽으로 90도 회전하고 이동했을 때 좌표
    print(point)
    if point not in old_point and board[x][y] == 0:       # 만약 해당 방향으로 이동한 좌표가 그전에 이동한 좌표가 아니고, 보드의 범위안에 들어오면 이동하고 좌표와 방향을 수정
        old_point.append(point)     # 이동했던 좌표를 추가
        cnt = 0     # 이동을 완료했으니 카운트를 초기화 후 다음 
        return x, y, d, cnt     #  이동한 방향과 좌표를 return
    
    else:       # 해당 방향으로 이동이 불가하므로 회전만 하고 좌표값은 그대로 유지 
        cnt += 1        # 방향을 회전했으므로 횟수를 일단 증가
        return a, b, d, cnt

def back_move(a, b, d):     # 방향을 다돌고 만약 이동할 방향이 없다면 뒤쪽 방향으로 움직이거나 움직임을 멈춰야함.
    if d == 0 :
        a += 1
    elif d ==1 :
        b -= 1
    elif d == 2:
        a -= 1
    elif d == 3:
        b += 1

    if board[a][b] == 0:    #회전을 다하고 이동할 방향이 없어서 방향을 유지하고 뒤로 움직여야하는데 그게 가능하면 go, 여기서 가봤던 곳으로 가기 때문에 따로 count x
        cnt = 0
        return a, b, d, 'go'
    else:       # 어느 방향으로도 움직일 수 없으니 stop
        return a, b, d, 'stop'
    
while 1:
    a, b, d, cnt = move(a, b, d, cnt)

    if cnt == 4:       # 왼쪽으로 돌았으나 갈곳이 없어서 일단 뒤로 움직여야 하는 상황
        a ,b ,d, word = back_move(a, b, d)      
        if word == 'stop':      # 뒤로 움직일라고 했으나 뒤에가 바다라 움직일 수 없음, 따라서 멈추고 이동했던 좌표들을 알려준다.
            print(len(old_point))
            break
        else:
            cnt = 0
        

        