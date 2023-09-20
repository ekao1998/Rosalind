# from Bio import SeqIO

# name = []
# seq = []


# for record in SeqIO.parse("/Users/ethankao/Downloads/rosalind_cons.txt", "fasta"):
#     name.append(record.id)
#     seq.append(str(record.seq))

# A=0
# T=0
# C=0
# G=0
# A_list = []
# T_list = []
# C_list = []
# G_list = []
# ans = []
# for i in range(len(seq[0])):
#     for k in seq:
#         if k[i] == "A":
#             A+=1
#         elif k[i] =="T":
#             T +=1
#         elif k[i] =="C":
#             C+=1
#         elif k[i] =="G":
#             G+=1
#     A_list.append(A)
#     T_list.append(T)
#     C_list.append(C)
#     G_list.append(G)
#     Dict = {A:"A",T:"T",C:"C",G:"G"}
#     Max = max(A,T,C,G)
#     ans.append(Dict[Max])
#     A=0
#     T=0
#     C=0
#     G=0
    
    




# joinConsensus = "".join(ans)


# print(joinConsensus)
# print("A: ", A_list)
# print("C: ", C_list)
# print("G: ", G_list)
# print("T: ", T_list)

from Bio import SeqIO

holdSeq=[] 
for record in SeqIO.parse("/Users/ethankao/Downloads/rosalind_cons.txt", "fasta"):
    holdSeq.append(record.seq)



index = len(holdSeq[0])
A=[]
T=[]
C=[]
G=[]

######### build_profile
for k in range(index): 
    A_count=0
    T_count=0
    C_count=0
    G_count=0
    for seq in holdSeq: #iterate every seq
        if seq[k] == "A":
            A_count+=1
        elif seq[k] == "T":
            T_count+=1
        elif seq[k] == "C":
            C_count+=1
        elif seq[k] == "G":
            G_count+=1
    A.append(str(A_count))
    T.append(str(T_count))
    C.append(str(C_count))
    G.append(str(G_count))

######### build_consensus

profileHold = [] #in A,T,C,G order
profileHold.append(A)
profileHold.append(T)
profileHold.append(C)
profileHold.append(G)

seqLen = len(holdSeq[0])
Consensus=[]
for i in range(seqLen): #this step is to iterate the index
    hold=[]
    for profileNum in profileHold: #in A,T,C,G order 
        hold.append(int(profileNum[i]))

    if hold.index(max(hold)) == 0: 
        Consensus.append("A")
        
    elif hold.index(max(hold)) == 1: 
        Consensus.append("T")

    elif hold.index(max(hold)) == 2: 
        Consensus.append("C")  

    elif hold.index(max(hold)) == 3: 
        Consensus.append("G")

  
       
  

######### formatting

joinConsensus = "".join(Consensus)
joinA = " ".join(A)
joinT = " ".join(T)
joinC = " ".join(C)
joinG = " ".join(G)

print(joinConsensus)
print("A: " + joinA)
print("C: " + joinC)
print("G: " + joinG)
print("T: " + joinT)