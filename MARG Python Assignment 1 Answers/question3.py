f = [0, 1, 0]
while f[2] < 10**8:
  print(f[2])
  f[0:2] = f[1:]
  f[2] = f[1] + f[0]