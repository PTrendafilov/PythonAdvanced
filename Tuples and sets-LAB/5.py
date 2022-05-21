n = int(input())
reserved = []
for i in range(n):
    reservation=input()
    reserved.append(reservation)
while 1:
    guests=input()
    if guests=="END":
        break
    elif guests in reserved:
        reserved.remove(guests)
reserved = sorted(reserved)
print(len(reserved))
for guest_not_came in reserved:
    print(guest_not_came)