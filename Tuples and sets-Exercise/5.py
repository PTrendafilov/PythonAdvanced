n=int(input())
max = 0
longest_interaction =[]
for i in range(0, n):
    s = input()
    s = s.split('-')
    numbers = []
    intersection_numbers=[]
    numbers_in_intersection_length = 0
    for el in s:
        el = el.split(',')
        numbers.append(int(el[0]))
        numbers.append(int(el[1]))
    for x in range(numbers[0], numbers[1]+1):
        for y in range(numbers[2],numbers[3]+1):
            if x==y:
                numbers_in_intersection_length+=1
                intersection_numbers.append(x)
            if max < numbers_in_intersection_length:
                max = numbers_in_intersection_length
                longest_interaction = intersection_numbers
print(f"Longest intersection is {longest_interaction} with length {max}")
