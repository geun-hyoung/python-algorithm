n, m = map(int, input().split())
weights = list(map(int, input().split()))
weights.sort()

i = n*(n-1)//2
s = 0
cnt = 0

for j in weights:
    if j == s:
        pass

    else:
        w = weights.count(j)
        if w == 1:
            pass

        else:
            cnt += w*(w-1)//2
            s = j

print(i - cnt)