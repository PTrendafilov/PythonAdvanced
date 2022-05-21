cars=[]
n = int(input())
for i in range(n):
    direction, car = input().split(', ')
    if direction == "IN" and car not in cars:
        cars.append(car)
    elif direction == "OUT" and car in cars:
        cars.remove(car)
for car in cars:
    print(car)
if not cars:
    print("Parking Lot is Empty")