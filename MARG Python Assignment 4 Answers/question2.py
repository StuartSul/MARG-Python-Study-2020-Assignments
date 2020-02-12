class Pixel:
    def __init__(self, color):
        self.checked = False
        self.color = color
        
def check_region(img, i, j):
    img[i][j].checked = True
    for _i, _j in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
        if 0 <= _i < len(img) and 0 <= _j < len(img[_i]) and\
          not img[_i][_j].checked and img[_i][_j].color == img[i][j].color:
            check_region(img, _i, _j)

width, height = map(int, input().split())

img = []
for i in range(height):
    img.append([])
    row = input()
    for j in range(width):
        img[i].append(Pixel(row[j]))

region_count = 0
for i in range(height):
    for j in range(width):
        if not img[i][j].checked:
            check_region(img, i, j)
            region_count += 1
print(region_count)