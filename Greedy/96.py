import sys
input = sys.stdin.readline

n, m = map(int, input().split())
 
# 첫번째 풀이법
num = 0 # 행의 가장 작은 수 와 지속적으로 비교하기 위한 상수 설정
for _ in range(n):  # 행의 횟수만큼 반복
    cards = list(map(int, input().split()))    
    line_min = min(cards)   # 행에서 가장 작은 값을 기록하고
        
    if line_min > num :     # 사전에 정의 해놓은 num 값과 비교하면서 진행
        num = line_min
    else:
        pass
print(num)      # 최종적으로는 행의 최솟값 중 가장 큰 값이 출력

# 두번째 풀이법
nums = []       # 행의 최솟값들을 저장한느 리스트
for _ in range(n):      
    cards = list(map(int, input().split()))
    nums.append(min(cards))

print(max(nums))    # 행의 수만큼 반복 후 그 중 가장 큰 수를 출력