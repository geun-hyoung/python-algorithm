s = list(map(int, list(input())))
l = len(s)
print(s)
result = []

for loc, value in enumerate(s):
    if loc == 0:
        result.append(value)
        pass
    if value == s[loc -1]:
        pass

    else:
        result.append(value)

print(min(result.count(0), result.count(1)))