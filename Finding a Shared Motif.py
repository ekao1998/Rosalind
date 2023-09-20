from Bio import SeqIO
from numpy import sort #import the biopython 
hold_list=[]
for seq_record in SeqIO.parse("/Users/ethankao/Downloads/rosalind_lcsm.txt", "fasta"):
    hold_list.append(str(seq_record.seq))

# print(hold_list)

# first need to sort all the seq from the shortest to the longest
sort_seq = sorted(hold_list, key = len)
# for x in sort_seq:
#     print(len(x)) 

short_seq = sort_seq[0] # the shortest in the sort_seq
remain_seq = sort_seq[1:]
motif = '' # initial the motif

for x in range(len(short_seq)): # start from the shortest's index 0
    for y in range(x,len(short_seq)): #iterate the index num
        possible = short_seq[x:y+1] #first set will be short_seq[0:1], [0:2] ..... check every possible combination
        for seq in remain_seq: #this part try to find the possible motif in every remain seq
            if possible in seq:
                pass # if found, pass, search in next seq
            else: # Once not found --> stop the search and erase the possible motif, stop the for loop
                possible = ''
                break
        if len(possible)>len(motif): # bc we want to find the longest motif so the longer one will be the new possible motif
            motif = possible

print(motif)

