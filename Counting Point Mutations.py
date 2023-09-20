with open("/Users/ethankao/Downloads/rosalind_hamm.txt") as f:
    lines = f.readlines()

line = []

for i in lines:
    line.append(i.rstrip())

count = 0
for i in range(len(line[0])):
    if line[0][i] != line[1][i]:
        count += 1

print(count)
