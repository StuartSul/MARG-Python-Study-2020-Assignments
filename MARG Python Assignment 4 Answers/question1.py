EMPTY = '0'
BLACK = '1'
WHITE = '2'
DIRECTIONS = [(0, 1), (1, 1), (1, 0), (1, -1)]

def is_defeat(board, i, j):
    for direction in DIRECTIONS:
        if count(board, i, j, direction) == 5:
            return True
    return False

def count(board, i, j, direction):
    total = 1
    for weight in [-1, 1]:
        for index in range(1, 4):
            _i = i + weight * index * direction[0]
            _j = j + weight * index * direction[1]
            if board[i][j] == board[_i][_j]:
                total += 1
            else:
                break
    return total

width, height = map(int, input().split())

board = []
for i in range(height):
    board.append(input())

for i in range(3, height - 3):
    for j in range(3, width - 3):
        if board[i][j] != EMPTY and is_defeat(board, i, j):
            print('{} wins!'.format('Black' if board[i][j] == BLACK else 'White'))
            quit(0)
print('Continue playing.')