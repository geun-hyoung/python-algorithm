def solution(s):

    words = list(s)
    result = []
    
    except_case = [10, 100, 1000]

    if len(words) == 1:
        return 1
    
    for i in range(1, len(words)//2 + 1):

        cnt = 0
        compress = ['@']

        for j in range(0, len(words), i):
            temp_word = "".join(words[j:j+i])

            if compress[-1] == temp_word:
                if temp_dict[temp_word] == 1:
                    cnt += 1

                temp_dict[temp_word] += 1
                temp_cnt = temp_dict[temp_word]
           
                if temp_cnt in except_case:
                    cnt += 1

            else:
                compress.append(temp_word)
                temp_dict = {temp_word:1}

        x = len(list("".join(compress)))

        result.append(x + cnt - 1)

    return min(result)

solution("aaaaaaaaaa")