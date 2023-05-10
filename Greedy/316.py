### 'https://school.programmers.co.kr/learn/courses/30/lessons/42891'
def solution(food_times, k):

    if sum(food_times) <= k:
        return -1
    
    length = len(food_times)
    
    temp_dict = {i:food_times[i] for i in range(len(food_times))}
    live_type = [i for i in range(length)]

    start = 0

    for i in range(0, k-1):

        if temp_dict[start] == 0:
            temp_dict.pop(start)

            live_type[start] = 0

        for i in range(start + 1, start+length + 1):
            if i >= length:
                finds = live_type[start-i]
            else:
                finds = live_type[i]

            if finds != 0:
                start = live_type.index(finds)
                break

    print(start)
    return start
            
        
solution([3,1,2], 5)
        