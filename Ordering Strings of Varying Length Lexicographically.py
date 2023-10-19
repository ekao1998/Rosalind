from itertools import product

string = "Q O S T R N Z H F M E C"
repeat_input = 3

# Remove spaces from the input string
input = "".join(string.split())
hold = []

# Generate all possible combinations
for i in range(1, repeat_input + 1):
    temp = product(input, repeat=i)
    for k in temp:
        hold.append(''.join(k))

# Define the custom order
custom_order = {char: index for index, char in enumerate(input)}

ans = sorted(hold, key=lambda x:tuple(custom_order[i] for i in x))

with open("ans.txt","x") as file:
    for x in ans:
        file.write(''.join(x))
        file.write("\n")

