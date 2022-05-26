rows, columns = input().split()
rows, columns = int(rows), int(columns)
matrix = []
for i in range(rows):
    row = [str(symbol) for symbol in input().split(' ')]
    matrix.append(row)
count_2X2 = 0
for row in range(rows - 1):
    for column in range(columns - 1):
        if matrix[row][column] == matrix[row + 1][column + 1] and matrix[row][column] == matrix[row][column + 1] \
                and matrix[row][column] == matrix[row + 1][column]:
            count_2X2 += 1
print(count_2X2)