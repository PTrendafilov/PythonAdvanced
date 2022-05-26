rows = int(input())
square = []
for i in range(rows):
    row = [int(number) for number in input().split(' ')]
    square.append(row)
primary_diagonal_sum = 0
for i in range(rows):
    primary_diagonal_sum+=square[i][i]
secondary_diagonal_sum=0
for i in range(rows-1, -1, -1):
    secondary_diagonal_sum+=square[i][rows-i-1]
if secondary_diagonal_sum>=primary_diagonal_sum:
    print(secondary_diagonal_sum-primary_diagonal_sum)
else:
    print(primary_diagonal_sum - secondary_diagonal_sum)
