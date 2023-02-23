loc = list(input())
x = list(map(int, [ord(loc[0])-96, loc[1]]))    # 열의 값이 알파벳으로 되어있기 때문에 아스키 코드를 이용해 전환
occations = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]    # 모든 케이스를 미리 저장
cnt = 0

for step in occations:
    row = step[0] + x[0]
    col = step[1] + x[1]

    if 0<row<9 and 0<col<9:     # 판 안에 들어오는지 확인 후 케이스 + 1
        cnt += 1
    else:
        pass

print(cnt)