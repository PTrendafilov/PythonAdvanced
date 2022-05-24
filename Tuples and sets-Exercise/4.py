text = input()
count_symbols = {}
for character in text:
    if character not in count_symbols:
        count_symbols[character] = 0
    count_symbols[character]+=1
for character in sorted(count_symbols.keys()):
    print(f"{character}: {count_symbols[character]} time/s")