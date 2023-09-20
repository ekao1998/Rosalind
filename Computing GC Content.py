from Bio import SeqIO

name = []
seq = []
gc = []

for record in SeqIO.parse("/Users/ethankao/Downloads/rosalind_gc.txt", "fasta"):
    name.append(record.id)
    seq.append(record.seq)



count = 0
total = 0
for i in seq:
    total += len(i)
    for k in i:
        if k == "C":
            count +=1
        elif k == "G":
            count +=1
    gc.append(count/total)
    count = 0
    total = 0


print(name[gc.index((max(gc)))],max(gc)*100)