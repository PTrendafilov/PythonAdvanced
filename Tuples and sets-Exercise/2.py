n, m = input().split()
n, m = int(n), int(m)
first_set = []
second_set = []
for i in range(n):
    first_set.append(input())
for i in range(m):
    second_set.append(input())
first_set = set(first_set)
second_set = set(second_set)
intersection_set = first_set.intersection(second_set)
for element in intersection_set:
    print(element)