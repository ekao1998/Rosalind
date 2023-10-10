from Bio import SeqIO #import the biopython 
hold_list=[]
for seq_record in SeqIO.parse("rosalind_sseq.txt", "fasta"):
    hold_list.append(str(seq_record.seq))

Sequence = hold_list[0]
SubSeq = hold_list[1]

Index = []
index_hold = -1 #initial to -1, no index can be smaller then this

for char in list(SubSeq):
    found = False
    count = 0 #start searching from first latter in the Sequence
    while not found: #running until found the proper index 
        if Sequence.index(char,count)>index_hold: 
            index_hold = Sequence.index(char,count) #update index hold, so not latter need to be bigger than this to mean the criteria
            Index.append(Sequence.index(char,count))
            found = True #if found stop the loop
        else:
            count+=1 


##Index num change to Indice need to add one
for num in Index:
    num +=1
    print(num, end=" ")