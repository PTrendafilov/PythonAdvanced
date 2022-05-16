from collections import deque
food = int(input())
que=deque([int(x) for x in input().split()])
print(max(que))
while que:
    if que[0]>food:
        break
    food -= int(que[0])
    que.popleft()
if que:
    print(f"Orders left: {' '.join(str(x) for x in que)}")
else:
    print(f"Orders complete")