import copy

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
temp_key = copy.deepcopy(key)

m = len(key)
n = len(lock)


result = []
result.append(key)

for _ in range(m):
    temp_key = copy.deepcopy(key)
    for i in range(m):
        for j, value in enumerate(key[i]):
            temp_key[j][m-i-1] = value
    
    result.append(temp_key)
    del key
    key = copy.deepcopy(temp_key)

return_list = []

for key in result:
    for length in range(0, m + n):
        for transverse in range(0, m + n):
            now = [i[length:length+n] for i in lock[transverse:transverse+n]]
            
            for i, j in enumerate(key, now):
                for k, l in enumerate(key, now):
                    if k == 1 and l == 1:
                        break
                    elif k == 0 and l == 0:
                        pass
                    elif k == 1 and l == 0:
                        pass
                    else:
                        now[j][l] = 0
        
