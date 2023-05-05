n, k = map(int, input().split())
count = 0

nums = n%k 

if nums != 0:
  n = n - nums
  m = nums
else:
  m = nums

while n>1:
  if n%k == 0:
    n //=k
  else:
    n -= 1
  count += 1
  
print(count)
print(m)