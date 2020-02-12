A, B = map(int, input().split())
a, b = A, B
while True:
  if a > b:
    b += B
  elif b > a:
    a += A
  else:
    print(a)
    break
