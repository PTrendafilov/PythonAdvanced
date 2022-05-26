rows, columns = input().split()
rows, columns = int(rows), int(columns)
matrix = []
for row_index in range(rows):
    row = []
    for column in range(columns):
        s = chr(ord('a')+row_index) + chr(ord('a')+row_index+column) + chr(ord('a')+row_index)
        row.append(s)
    matrix.append(row)
# print(matrix)
for row in range(rows):
    for column in range(columns):
        print(matrix[row][column], end=" ")
    print()