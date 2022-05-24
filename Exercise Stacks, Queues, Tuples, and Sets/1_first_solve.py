first_set = set(int(number) for number in input().split())
second_set = set(int(number) for number in input().split())
n = int(input())
for i in range(n):
    command = input().split()
    if command[0] == "Add":
        if command[1] == "First":
            for i in range(2,len(command)):
                first_set.add(int(command[i]))
        else:
            for i in range(2, len(command)):
                second_set.add(int(command[i]))
    elif command[0]=="Remove":
        if command[1] == "First":
            for i in range(2,len(command)):
                if int(command[i]) in first_set:
                    first_set.remove(int(command[i]))
        else:
            for i in range(2,len(command)):
                if int(command[i]) in second_set:
                    second_set.remove(int(command[i]))
    else:
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            print("True")
        else:
            print("False")
print(*sorted(first_set),sep=", ")
print(*sorted(second_set), sep=", ")