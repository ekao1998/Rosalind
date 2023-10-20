RNA = "UGCUGCGCCAUAGCUUACUGACCGAGUGAUCACAGGCCUAAUGUAGGCCGUCCACUGGAAGACCGCUCCUGAGUGG"

count_AU =0
count_GC =0

for i in range(len(RNA)):
    if RNA[i] =="A":
        count_AU+=1
    elif RNA[i] =="C":
        count_GC+=1



from math import factorial
print(factorial(count_GC)*factorial(count_AU))
    