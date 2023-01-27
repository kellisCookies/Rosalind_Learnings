import math

"""
The Rosalind solution:

def permutations(l):
    return [ (m[:i] + [l[0]] + m[i:]) for m in permutations(l[1:]) for i in xrange(len(m)+1) ] if len(l)>1 else [l]

p = permutations(range(1,n+1))

print len(p)
for l in p:
    print ' '.join(map(str,l))

"""

def swapNumbers(array,idx, idx2):
    lastnum = array[idx]
    secondtolastNum= array[idx2]
    newArray = list(array)
    newArray[idx] = secondtolastNum
    newArray[idx2] = lastnum
    return newArray


def iteratenumbersDown(result_array, arrayRefRow, holdposition,n):
    swapPosition = holdposition +1
    for x in range(1,n-holdposition):
        result_array.append(list(swapNumbers(result_array[arrayRefRow],holdposition, swapPosition)))
        swapPosition = swapPosition+1
    return result_array

def permutation(n):
    numPermutations = math.factorial(n)
    print(numPermutations)
    currentArray=[]        
    result_array = []
    #create and initialized array and add it to the list 
    for i in range(n):
        currentArray.append(i+1)
    result_array.append(list(currentArray))
    holdposition = 0

    while holdposition < n-1:
        #move down each position, and itterate through swapping that position with the numbers down the line
        for x in range(len(result_array)):
            new_array = iteratenumbersDown(result_array, x, holdposition,n)
        holdposition = holdposition + 1
        
    print('\n'.join(' '.join('%2d' % x for x in y) for y in result_array))
    return (numPermutations, result_array)

permutation(6)