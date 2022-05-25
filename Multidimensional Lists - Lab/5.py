rows = int(input())
arr = []
for i in range(rows):
    numbers = [int(x) for x in input().split(' ')]
    arr.append(numbers)
sum =0
for i in range(rows):
    sum+=arr[i][i]
print(sum)
