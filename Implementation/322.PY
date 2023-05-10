word = list(input())
str_arr = []
int_arr = []

for x in word:
    try:
        int_arr.append(int(x))
    except:
        str_arr.append(x)

str_arr.sort()
int_arr.sort()

print(*str_arr, *int_arr, sep='')