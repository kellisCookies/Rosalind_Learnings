from math import comb
"""
Given: 
    Two positive integers (k≤7) and N(N≤2k). In this problem, we begin with Tom, 
    who in the 0th generation has genotype Aa Bb. Tom has two children in the 1st generation, 
    each of whom has two children, and so on. Each organism always mates with an organism having genotype Aa Bb.

Return: 
    The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family tree 
    (don't count the Aa Bb mates at each level). 
    Assume that Mendel's second law holds for the factors."""

"""Strategy:

    1. Anytime an Aa is mated with any other genotype (AA or aa) there will always be a 0.5 chance of being Aa
    2. The probability of an AaBa baby therefore (0.5)*(0.5) = 0.25, no matter what an AaBb is mated to
    3. The odds of a child not bing AaBb is 1-0.25 = 0.75
    4. the odds that at least 1 person has AaBb = 1 - P(0)
            the odds that at least 2 people has AaBb = 1- [P(0) + P(1)]
            P(>=3 AaBb) = 1- [P(0) + P(1) + P(2)]
            P(>=N AaBb) = 1- [P(0) + P(1)+ P(N-1)]
    5.  P(0) = (0.25)^0 x (0.75)^ngen    #need to also multiply by the number of combinations this can occur and divide by total combinations
        P(1) = (0.25)^1 x (0.75)^ngen-1  #need to also multiply by the number of combinations this can occur and divide by total combinations
        P(2) = (0.25)^2 x (0.75)^ngen-2  #need to also multiply by the number of combinations this can occur and divide by total combinations
        etc...
"""

def probDecendantsAaBb(k,N):
    ngen = 2**k #number of people in the kth generation
    prob = 0
    #Sum the probability that 0, 1, ...N people do NOT have AaBb then subtract from 1 to fine AT LEAST N has it  
    for x in range(N):
        prob += (((0.25)**x)*((0.75)**(ngen-x))*comb(ngen,x))/comb(ngen,ngen)
    return 1-prob    

n = probDecendantsAaBb(6,16)
print(round(n,3))