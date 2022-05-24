numbers = [int(x) for x in input().split()]
unique_pairs = []
target_number = int(input())
iterations = 0
for i in range(len(numbers)):
    for second_number in numbers[i+1:len(numbers)]:
        if numbers[i]+second_number==target_number:
            print(f"{numbers[i]} + {second_number} = {target_number}")
            pair = numbers[i], second_number
            if pair not in unique_pairs:
                unique_pairs.append(pair)
        iterations+=1
print(f"Iterations done: {iterations}")
for pair in unique_pairs:
    print(pair)