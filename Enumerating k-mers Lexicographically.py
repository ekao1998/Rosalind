from itertools import product

input = 'ABCDEFGH'
repeat_input = 3

ans = list(product(input, repeat = repeat_input))

for x in ans:
    print(''.join(x))