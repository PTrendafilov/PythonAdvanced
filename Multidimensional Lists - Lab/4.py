rows, columns = input().split(', ')
rows, columns = int(rows), int(columns)
arr = []
for i in range(rows):
    numbers = [int(x) for x in input().split(' ')]
    arr.append(numbers)
for i in range(columns):
    sum = 0
    for j in range(rows):
        sum+=arr[j][i]
    print(sum)
