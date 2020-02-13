def is_defeat(board, i, j):
    directions = [(0, 1), (1, 1), (1, 0), (1, -1)]
    for direction in directions:
        total = 1
        for weight in [-1, 1]:
            for index in range(1, 4):
                _i = i + weight * index * direction[0]
                _j = j + weight * index * direction[1]
                if board[i][j] == board[_i][_j]:
                    total += 1
                else:
                    break
        if total == 5:
            return True
    return False

width, height = map(int, input().split())

board = []
for i in range(height):
    board.append(input())

for i in range(3, height - 3):
    for j in range(3, width - 3):
        if board[i][j] != '0' and is_defeat(board, i, j):
            print('{} wins!'.format('Black' if board[i][j] == '1' else 'White'))
            quit(0)
print('Continue playing.')