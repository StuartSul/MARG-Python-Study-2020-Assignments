img_file = open('MARG Python Assignment 3 (Data).csv', 'r')
img = img_file.read()
img_file.close()

img = img[:-1].split('\n')
img = [x.split(',') for x in img]

img = img[::2]
for i in range(len(img)):
  img[i] = img[i][::2]
  for j in range(len(img[i])):
    img[i][j] = int(img[i][j]) / 255

data = ''
for row in img:
  for elem in row:
    data += str(elem) + ','
data = data[:-1]

new_img_file = open('output.txt', 'w')
new_img_file.write(data)
new_img_file.close()