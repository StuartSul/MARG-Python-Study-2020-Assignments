f = list(map(int, input().split()))
x = int(input())
y = 0
for i in range(0, len(f) - 1):
  y += f[i] * (len(f)-i-1) * x**(len(f)-i-2)
print(y)