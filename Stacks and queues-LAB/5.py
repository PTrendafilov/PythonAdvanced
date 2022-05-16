from collections import deque
people = deque(input().split())
n=int(input())
current_count=0
while len(people)>1:
    current_count+=1
    person=people.popleft()
    if current_count<n:
        people.append(person)
    else:
        print(f"Removed {person}")
        current_count-=n
        #print(people)
print(f"Last is {people[0]}")