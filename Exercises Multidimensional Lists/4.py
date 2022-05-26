rows, columns = input().split()
rows, columns = int(rows), int(columns)
matrix = []
for i in range(rows):
    row = [int(number) for number in input().split(' ')]
    matrix.append(row)
max_sum = matrix[0][0] + matrix[0][1] + matrix[0][2] + matrix[1][0] + matrix[1][1] + matrix[1][2] \
          + matrix[2][0] + matrix[2][1] + matrix[2][2]
max_square = []
for row in range(rows - 2):
    for column in range(columns - 2):
        square = [matrix[row][column],
                  matrix[row][column + 1],
                  matrix[row][column + 2],
                  matrix[row + 1][column],
                  matrix[row + 1][column + 1],
                  matrix[row + 1][column + 2],
                  matrix[row + 2][column],
                  matrix[row + 2][column + 1],
                  matrix[row + 2][column + 2]]
        square_sum = 0
        for number in square:
            square_sum += number
        if square_sum > max_sum:
            max_sum = square_sum
            max_square = square
if max_square==[]:
    square = [matrix[0][0], matrix[0][1], matrix[0][2], matrix[1][0], matrix[1][1], matrix[1][2], matrix[2][0],
              matrix[2][1], matrix[2][2]]
    max_square = square
print(f"Sum = {max_sum}")
# print(square)
for i in range(9):
    print(max_square[i], end=" ")
    if i % 3 == 2:
        print()
# print(max_square)
