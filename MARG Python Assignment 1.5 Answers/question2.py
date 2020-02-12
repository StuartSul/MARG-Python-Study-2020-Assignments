numbers = list(map(int, input().split()))
s = 0
for i in range(len(numbers)):
    s += (i + 1) * numbers[i]
print(s)