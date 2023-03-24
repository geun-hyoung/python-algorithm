arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def change_str(num):
    return ' '.join([arr[i] for i in list(map(int, str(num)))])

def change_int(word):
    return int(''.join(str(arr.index(i)) for i in word.split()))

n, m = map(int, input().split())

words = sorted([change_str(i) for i in range(n, m + 1)])

for j in range(0, len(words), 10):
    print(*[change_int(i) for i in words[j:j+10]])