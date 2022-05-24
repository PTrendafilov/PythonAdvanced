n = int(input())
table = []
for i in range(n):
    chemical_elements = input().split()
    for chemical_element in chemical_elements:
        if chemical_element not in table:
            table.append(chemical_element)
for chemical_element in table:
    print(chemical_element)