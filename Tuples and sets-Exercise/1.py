names=[]
n = int(input())
for i in range(n):
    name=input()
    if name not in names:
        names.append(name)
for name in names:
    print(name)