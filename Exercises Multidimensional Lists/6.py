rows, columns = input().split()
rows, columns = int(rows), int(columns)
matrix = []
for row_index in range(rows):
    row = [str(element) for element in input().split()]
    matrix.append(row)
while 1:
    command = input()
    if command == "END":
        break
    else:
        command = command.split()
        if command[0] == 'swap':
            if command[1].isnumeric() and command[2].isnumeric() and command[3].isnumeric() and command[4].isnumeric():
                row_first_element = int(command[1])
                col_first_element = int(command[2])
                row_second_element = int(command[3])
                col_second_element = int(command[4])
                if row_first_element < rows and row_second_element < rows and col_first_element < columns and \
                col_second_element < columns:
                    temp = matrix[row_first_element][col_first_element]
                    matrix[row_first_element][col_first_element] = matrix[row_second_element][col_second_element]
                    matrix[row_second_element][col_second_element] = temp
                    for row in range(rows):
                        for col in range(columns):
                            print(matrix[row][col], end=" ")
                        print()
                else:
                    print('Invalid input!')
            else:
                print('Invalid input!')
        else:
            # print(command[0])
            print('Invalid input!')
