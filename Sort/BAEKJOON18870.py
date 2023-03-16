##https://www.acmicpc.net/problem/18870
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

array = sorted(list(set(nums)))
dic = {array[i]: i for i in range(len(array))}

for i in nums:
    print(dic[i], end = ' ')
