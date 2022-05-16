import sys

n=int(input())
stack=list()
min = sys.maxsize
max= -sys.maxsize
for i in range(n):
    query=input()
    if query.isnumeric():
        if int(query)==2:
            if stack:
                stack.pop()
        elif int(query)==4 and stack:
            for num in stack:
                num=int(num)
                if num<min:
                    min=int(num)
            print(min)
        elif int(query)==3 and stack:
            for num in stack:
                if int(num)>max:
                    max=int(num)
            print(max)
    else:
        query = query.split(' ')
        stack.append(query[1])
for i in range(len(stack)-1, -1, -1):
    if i!=0:
        print(stack[i],end=', ')
    else:
        print(stack[i])