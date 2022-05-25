rows, columns = input().split(", ")
rows, columns = int(rows), int(columns)
arr = []
sum = 0
for i in range(rows):
    numbers = [int(x) for x in input().split(', ')]
    for number in numbers:
        sum+=number
    arr.append(numbers)
print(sum)
print(arr)


