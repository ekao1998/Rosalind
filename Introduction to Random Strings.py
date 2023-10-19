import math

DNA = "TTCCACAACACAGTCACTAATATAACTACACCCTGACTGATGGGTGCGTTCAATCCTTGGCTCTATAATCTACAAGCCGCGCT"
number_line = "0.073 0.144 0.192 0.244 0.273 0.343 0.374 0.449 0.497 0.544 0.592 0.653 0.710 0.748 0.808 0.873 0.909"
gc_content = [float(i) for i in number_line.split()]


outputs = []
prob = 0
for i in gc_content:
    prob = 0
    chances = {
        'A' : (1-i)/2,
        'C' : i/2,
        'G' : i/2,
        'T' : (1-i)/2
    }
    for j in DNA:
        prob += math.log10(chances[j])
    outputs.append(prob)


print(" ".join([str(i) for i in outputs]))