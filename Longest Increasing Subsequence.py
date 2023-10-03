import math

with open("rosalind_lgis.txt","r") as file:
    size=int(file.readline().strip()) ##line 1

    ##line 2
    list=[] #this is for increasing 
    for x in file.readline().strip().split(' '):
      list.append(int(x))
  
    reverselist=[] #this is for decreasing
    for x in list:
      reverselist.append(-1*x) #--> will change the data to -5 -1 -4 -2 -3

def lgis(string): ##bc our function is for incresing subsequence so in line 34 we need ro convert the data in -, t ofit this function 
    p=[0]*size
    m=[0]*(size+1)

    l=0

    for i in range(size):
        lo=1
        hi=l
        while lo<=hi:
            mid=math.floor((lo+hi)/2)
            if string[m[mid]]<string[i]:
                lo = mid+1
            else:
                hi = mid-1
        newL = lo
        p[i]=m[newL-1]
        m[newL] = i
        if newL>l:
            l=newL

    s=[0]*l
    k=m[l]
    for i in reversed(range(l)):
        s[i]=string[k]
        k=p[k]
    return s

print(' '.join(map(str,lgis(list)))) #increasing 
print(' '.join(map(str,[-1*x for x in lgis(reverselist)]))) #reverse the data from -5 -1 -4 -2 -3 back to 5 1 4 2 3 
