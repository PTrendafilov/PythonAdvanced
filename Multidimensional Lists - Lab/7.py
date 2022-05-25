rows, columns = input().split(", ")
rows, columns = int(rows), int(columns)
arr = []
for i in range(rows):
    numbers = [int(number) for number in input().split(', ')]
    arr.append(numbers)
max = arr[0][0]+arr[0][1]+arr[1][0]+arr[1][1]
max_square = []
for i in range(rows-1):
    for j in range(columns-1):
        square = []
        square.append([arr[i][j], arr[i+1][j]])
        square.append([arr[i][j+1], arr[i+1][j+1]])
        sum_square = arr[i][j]+arr[i][j+1]+arr[i+1][j]+arr[i+1][j+1]
        if max<sum_square:
            max_square.append(square)
            max = sum_square
#print(max_square[len(max_square)-1])
for j in range(2):
    for i in range(2):
        print(max_square[len(max_square)-1][i][j], end = " ")
    print()
print(max)