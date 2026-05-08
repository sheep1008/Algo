letter = 0
digit = 0
s = input()

for c in s:
    if c.isdigit(): digit+=1
    elif c.isalpha(): letter += 1
        
print(f"LETTERS {letter}")
print(f"DIGITS {digit}")