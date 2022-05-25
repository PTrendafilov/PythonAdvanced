rows = int(input())
arr = []
for i in range(rows):
    numbers = [int(x) for x in input().split(', ')]
    even_numbers = []
    for i in range(0, len(numbers)):
        if numbers[i]%2==0:
            even_numbers.append(numbers[i])
    arr.append(even_numbers)
print(arr)
