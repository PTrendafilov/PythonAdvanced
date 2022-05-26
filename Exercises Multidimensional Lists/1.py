rows = int(input())
square = []
for i in range(rows):
    row = [int(number) for number in input().split(', ')]
    square.append(row)
primary_diagonal = []
secondary_diagonal = []
primary_diagonal_sum = 0
for i in range(rows):
    primary_diagonal.append(str(square[i][i]))
    primary_diagonal_sum+=square[i][i]
# print(primary_diagonal)
secondary_diagonal_sum=0
for i in range(rows-1, -1, -1):
    secondary_diagonal.append(str(square[i][rows-i-1]))
    secondary_diagonal_sum+=square[i][rows-i-1]
secondary_diagonal.reverse()
# print(secondary_diagonal)
print(f"Primary diagonal: {', '.join(primary_diagonal)}. Sum: {primary_diagonal_sum}")
print(f"Secondary diagonal: {', '.join(secondary_diagonal)}. Sum: {secondary_diagonal_sum}")
