# from Bio import SeqIO

# name = []
# seq = []

# for record in SeqIO.parse("/Users/ethankao/Downloads/rosalind_grph.txt", "fasta"):
#     name.append(record.id)
#     seq.append(str(record.seq))

# table = {}

# for i in range(len(name)):
#     overlap = []
#     overlap.append(seq[i][0:3])
#     overlap.append(seq[i][-3:])
#     table[name[i]] = overlap



# key = list(table.keys())
# print(key)
# for i in range(len(key)):
#     p1 = table[key[i]]
#     for k in range(i+1,len(key)):
#         p2 = table[key[k]]

#         for j in range(len(p1)):
#             if j ==0 and p1[j] == p2[1]:
#                 print(key[i]+" "+key[k])
#             elif j ==1 and p1[j] == p2[0]:
#                 print(key[i]+" "+key[k])




from copy import copy
from Bio import SeqIO #import the biopython 
hold_list=[]
for seq_record in SeqIO.parse("/Users/ethankao/Downloads/rosalind_grph.txt", "fasta"):
    hold_list.append([seq_record.id,seq_record.seq[:3],seq_record.seq[-3::]])


hold_name = ''
hold_front = ''
hold_end = ''

for k in hold_list:
    compare_list = copy(hold_list)
    hold_name = k[0] 
    hold_front = k[1]
    hold_end = k[2]
    compare_list.remove(k) #remove first [set] in the hold_list
    
    for l in compare_list: #and compare the rest of the list to the hold( name, front ,end )

        if hold_end ==l[1]:
            print(hold_name +' '+l[0])
