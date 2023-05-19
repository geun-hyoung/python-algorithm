### 'https://school.programmers.co.kr/learn/courses/30/lessons/42891'
def solution(food_times, k):

    types = len(food_times)
    food_dict = {i:food_times[i] for i in range(types)}

    step = 0
    while True:

        if food_dict[step] != 0:
            pass

        else:
            for i in range(step+1, step + types + 1):
                temp_step = i%types
                if food_dict[temp_step] != 0:
                    step = temp_step
                    break
                else:
                    if i == step + types:
                        return -1
                    pass

        food_dict[step] -= 1
        step = (step + 1)%types
        k -= 1

        if k == 0:
            break
        
    return step + 1

solution([3,1,2], 5)
        