from Bio import SeqIO
hold = []
for seq_record in SeqIO.parse("rosalind_splc.txt", "fasta"):
    hold.append(str(seq_record.seq))

sample = hold[0]
introns = hold[1:]

rm_intron = sample
for i in introns:
    temp=rm_intron.split(i)
    rm_intron = "".join(temp)


from Bio.Seq import Seq
rna = Seq(rm_intron)
my_aa = rna.translate()
print(my_aa)