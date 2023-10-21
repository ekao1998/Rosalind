n = 4

hold = [] # positive and negative number
for i in range(1,n+1):
    hold.append(i)
    hold.append(-i)


from itertools import permutations
possible_prem = list(permutations(hold,n))

ans = []

# test=[abs(i) for i in possible_prem[0]]
# print(test)
# print(set(test))

for i in range(len(possible_prem)):
    test=[abs(k) for k in possible_prem[i]] # change num to abs and try to find repeat one
    if len(set(test)) != n: # rm the repeat one, if len != to n then fail the question condition
        pass
    else:
        ans.append(possible_prem[i])

print(len(ans))
for i in ans:
    print(*i)