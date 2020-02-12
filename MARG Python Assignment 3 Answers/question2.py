img, data = [x.split(',') for x in open('MARG Python Assignment 3 (Data).csv', 'r').read()[:-1].split('\n')], ''
for i in range(0, len(img), 2):
  for j in range(0, len(img[i]), 2):
    data += str(int(img[i][j]) / 255) + ','
open('output.txt', 'w').write(data[:-1])