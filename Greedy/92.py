import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())     ## 입력 부분
array = list(map(int, input().split()))

num_1 = max(array)      # 가장 큰 수를 저장
array.remove(num_1)     # 반복 횟수에 제한이 있기 때문에 그 다음 수를 저장하기 위한 제거
num_2 = max(array)      # 두번째로 큰 수를 저장

counts = m%k      #  가장 큰 수를 k번 반복하고 그 다음에는 두번째로 작은 수인 num_2가 와야함 따라서 그 횟수를 구해주기 위해 나머지를 계산
a = m//k        # k번 반복하는 과정이 총 몇번인지를 계산하기 위함.
sum = (num_1*a*k) + (num_2*counts)      # 동빈이의 큰 수 법칙에 따라 계산하기 위함.
print(sum)