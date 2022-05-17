clothes = list(int(x) for x in input().split())
rake = int(input())
current_clothes=0
br=1
while clothes:
    clothe = clothes.pop()
    current_clothes+=clothe
    if current_clothes>rake:

        clothes.append(clothe)
        #print(clothes)
        current_clothes = 0
        br+=1
print(br)