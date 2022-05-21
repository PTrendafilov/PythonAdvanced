numbers_dict={}
numbers=[float(x) for x in input().split()]
for x in numbers:
    if x not in numbers_dict:
        numbers_dict[x]=0
    numbers_dict[x]+=1
for x, count in numbers_dict.items():
    print(f"{x} - {count} times")