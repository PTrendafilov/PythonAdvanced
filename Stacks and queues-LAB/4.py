from collections import deque
que = deque()
water_in_dispenser = int(input())
while 1:
    person=input()
    if person=="Start":
        break
    else:
        que.append(person)
while 1:
    command=input()
    if command.isnumeric():
        command=int(command)
        if command<=water_in_dispenser:
            water_in_dispenser-=command
            print(f"{que.popleft()} got water")
        else:
            print(f"{que[0]} must wait")
            que.popleft()
    else:
        if command=="End":
            print(f"{water_in_dispenser} liters left")
            break
        else:
            command=command.split(" ")
            #print(command[1])
            water_in_dispenser+=int(command[1])