from collections import deque
que=deque()
while True:
    customer=input()
    if customer=="Paid":
        while que:
            print(que.popleft())
    elif customer=="End":
        print(f"{len(que)} people remaining.")
        break
    else:
        que.append(customer)