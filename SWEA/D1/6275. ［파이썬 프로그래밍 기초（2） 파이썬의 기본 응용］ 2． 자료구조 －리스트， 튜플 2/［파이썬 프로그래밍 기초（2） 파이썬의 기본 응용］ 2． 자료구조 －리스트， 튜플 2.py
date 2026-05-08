s = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
ae = {'a', 'e', 'i', 'o', 'u'}
answer = [c for c in s if c not in ae]

print(''.join(answer))