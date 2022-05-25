rows = int(input())
arr = []
for i in range(rows):
    word = input()
    arr.append(word)
searched_symbol = input()
flag = False
for i in range(rows):
    if flag:
        break
    for j in range(rows):
        if searched_symbol == arr[i][j]:
            print(f"({i}, {j})")
            flag = True
if flag==False:
    print(f"{searched_symbol} does not occur in the matrix")