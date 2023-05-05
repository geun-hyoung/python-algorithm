import sys
input = sys.stdin.readline

n = int(input())

time_table = []
lec_times = [0] * n


for i in range(n):

    times = list(map(int, input().split()))
    times.remove(-1)
    time_table.append([i] + times)

time_table.sort(key = lambda x : len(x))

while True:
    print('hello')
    if 0 not in lec_times:
        break

    for time in time_table:
        x = time[0]

        if lec_times[x] != 0:
            pass

        else:
            if len(time) == 2:
                lec_times[time[0]] = time[1]

            else:
                do_lec = time[2:]

                arr = [lec_times[i - 1] for i in do_lec]

                if 0 in arr:
                    pass

                else:
                    temp_times = max(arr)
                    lec_times[x] = temp_times + time[1]

print(lec_times)







