first_set = set(int(number) for number in input().split())
second_set = set(int(number) for number in input().split())
n = int(input())
for i in range(n):
    command = input().split()
    if command[0] == "Add":
        if command[1] == "First":
            first_set=first_set.union([int(x) for x in command[2:]])
        else:
            second_set=second_set.union([int(x) for x in command[2:]])
    elif command[0]=="Remove":
        if command[1] == "First":
            first_set=first_set.difference([int(x) for x in command[2:]])
        else:
            second_set=second_set.difference([int(x) for x in command[2:]])
    else:
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            print("True")
        else:
            print("False")
print(*sorted(first_set),sep=", ")
print(*sorted(second_set), sep=", ")