import sys
input = sys.stdin.readline

def element(info):
    return int(info[1])

infos = sorted([list(input().rstrip().split()) for _ in range(int(input()))], key=element)
for i in infos: print(i[0], end=' ')


