target = 83
perMut = 8

# count the actural permutaitons
# from itertools import permutations

# perm = permutations(list(range(1,target+1)),perMut)

# print(len([*perm])%1000000)

"""
The statistic P(n,k)
 counts the total number of partial permutations of k
 objects that can be formed from a collection of n
 objects. Note that P(n,n)
 is just the number of permutations of n
 objects, which we found to be equal to n!=n(n−1)(n−2)⋯(3)(2)

"""
partial = 1 
for i in range(perMut):
    partial *= (target - i)

print(partial%1000000)