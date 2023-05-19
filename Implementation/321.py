words = list(map(int, list(input())))

cri = len(words)//2

if sum(words[0:cri]) == sum(words[cri:]):
    print('LUCKY')
else:
    print('READY')


if 6:
    print('hello')