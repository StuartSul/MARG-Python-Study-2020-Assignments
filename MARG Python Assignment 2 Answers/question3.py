def answer(number):
  count = 0
  for digit in str(number):
    if digit == '3' or digit == '6' or digit == '9':
      count += 1
  if count > 0:
    return 'clap' * count
  else:
    return str(number)

number = 1
while True:
  print(answer(number))
  if input() != answer(number + 1):
    print('You lost!')
    break
  number += 2