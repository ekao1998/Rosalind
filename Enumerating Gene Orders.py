from itertools import permutations

sample = 5

perm = permutations(range(1,sample+1))
count = 0
perm_hold = []
for i in perm:
    count+=1
    format_string = " ".join(map(str, i)) # convert tuple to string, and replace "," to " "
    perm_hold.append(format_string)

with open("aa.txt","w") as file:
    file.write(str(count))
    file.write("\n")
    for i in perm_hold:
        file.write(str(i))
        file.write("\n")



