rows = int(input())
arr = []
for i in range(rows):
    numbers = [int(x) for x in input().split(', ')]
    for number in numbers:
        arr.append(number)
print(arr)
