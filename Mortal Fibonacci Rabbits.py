def MortalFibonacci(n, m):
    # generations, need one month to mature
    living = [1, 1] 
    for i in range(2, n):
        # first reproduction
        tmp = living[i - 1] + living[i - 2]
        # then death
        if i == m:
            tmp = tmp - 1
        if i > m:
            tmp = tmp - living[i - m - 1]
        living.append(tmp)
    return living[-1]

# months/generations
n = 95
# survival time
m = 17

print(MortalFibonacci(n, m))