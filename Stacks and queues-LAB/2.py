s=list(input())
stack=[]
for i in range(0,len(s)):
    if s[i]=='(':
        stack.append(i)
    elif s[i]==')':
        print(''.join(s[stack[len(stack)-1]:i+1]))
        stack.pop()