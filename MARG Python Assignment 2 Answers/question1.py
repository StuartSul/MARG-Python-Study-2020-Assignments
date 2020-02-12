f = list(map(int, input().split()))
x = int(input())
y = 0
for i in range(len(f)):
  y += f[i] * x**(len(f)-i-1)
print(y)