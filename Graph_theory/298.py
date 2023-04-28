import sys

input = sys.stdin.readline
n, m = map(int, input().split())


teams = [i for i in range(n + 1)]



for _ in range(m):
    t, a, b = map(int, input().split())
    
    if t == 0 :
        num_1 = teams[a]
        num_2 = teams[b]
        temp_num = min(num_1, num_2)
        change_num = max(num_1, num_2)

        for i, j in enumerate(teams):
               if j == change_num:
                    teams[i] = temp_num
        
    elif t == 1:
        if teams[a] == teams[b]:
            print('YES')
        else:
            print('NO')

print(teams)