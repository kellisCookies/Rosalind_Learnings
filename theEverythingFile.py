import re
import math
import numpy as np
import csv

string1= "AGGACACTG"


def count_transcribe(string1):
    string2=""
    result_array=[0,0,0,0]
    for x in string1:
        if x == "A":
            result_array[0] = result_array[0]+1
            string2 = string2 + "A"
        if x =="C":
            result_array[1] = result_array[1]+1
            string2 = string2 + "C"
        if x == "G":
            result_array[2] = result_array[2]+1
            string2 = string2 + "G"
        if x == "T":
            result_array[3] = result_array[3]+1
            string2 = string2 + "U"
    return (result_array, string2)

def complement(string1):
    string2=""
    result_array=[0,0,0,0]
    for x in string1:
        if x == "A":
            result_array[0] = result_array[0]+1
            string2 = string2 + "T"
        if x =="C":
            result_array[1] = result_array[1]+1
            string2 = string2 + "G"
        if x == "G":
            result_array[2] = result_array[2]+1
            string2 = string2 + "C"
        if x == "T":
            result_array[3] = result_array[3]+1
            string2 = string2 + "A"
    return (string2)

def reverse(string):
    bwdString=""
    bwdString = string[::-1]
    return(bwdString)


def crazy_rabbits_recursive(n,k):
    #(int1, k):
    """ MY VERSION
    x=2
    rabbitSequence= []
    rabbitSequence.append(1)
    rabbitSequence.append(1)

    while x < int1:
        rabbitSequence.append(rabbitSequence[x-2]*k + rabbitSequence[x-1])
        x=x+1
    print(rabbitSequence)"""
    x0, x1 = 1, 1
    for i in range(2,n):
        x0, x1 = x1, k*x0 + x1
    print (x1)

def swapNumbers(array,idx, idx2):
    lastnum = array[idx]
    secondtolastNum= array[idx2]
    newArray = list(array)
    newArray[idx] = secondtolastNum
    newArray[idx2] = lastnum
    return newArray

def permOfThree (result_array, arrayReference,permIndex, n):
    counter = 1
    numPermutations = 6
    numberOfCycles = n-3+1
    
    while permIndex <= numPermutations:
        if (permIndex % 2) == 0:
            #if even swap the last two numbers
            """ 2 3 4 
                2 4 3
                """
            new_array = []
            new_array = swapNumbers(result_array[permIndex-2],n-1, n-2)
            result_array[permIndex-1] = list(new_array)
            permIndex = permIndex +1
            counter = counter + 1
        else:
            #change the idx from back to the next number then move on
            new_array = []
            new_array = swapNumbers(list(result_array[arrayReference]),n-3,numberOfCycles)
            numberOfCycles = (numberOfCycles+1)%(3) 
            counter = counter +  1
            result_array[permIndex-1] = list(new_array)
            permIndex = permIndex +1
    return(result_array)

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

def probabiliyDominant(k,m,n):
    #k is DD
    #m is Dd
    #n is dd
    Total = k + n + m
    T = Total * (Total - 1)
    print(T)
    #Dd x Dd
    firstTerm = (m*(m-1))/4
    secondTerm = (m*n)
    thirdTerm = n*(n-1)

    probreccessive = (1/T) *(firstTerm + secondTerm + thirdTerm)

    probDom = 1-probreccessive
    return probDom

def cgpercent(fasta):
    """Returns the percentage of Cs and Gs in a string"""
    cg = 1
    perc = 0
    total = 1
    firsttime = True
    with open(fasta, 'r') as file:
        csvreader = csv.reader(file)
        
        for line in csvreader:
            #ACGU
            if line[0][0] == ">":
                if firsttime == False:
                    perc = cg / total
                    print(round(perc*100,6))
                    total = 0
                    cg = 0
                print(line[0])
            else:
                firsttime=False
                array = []
                array, transcribe = count_transcribe(line[0])
                total = total + array[0] + array[1] + array[2] + array[3]
                cg = cg + array[1] + array[2]
        perc = cg / total
        print(round(perc*100,6))

def hammingDist(string1, string2):
    hammingnum = 0
    for index, letter in enumerate(string1):
        if letter != string2[index]:
            hammingnum = hammingnum + 1
    print(hammingnum)
    

def turnTextToLookupTable():
    rnaDict = {}
    reader = csv.reader(open(r"C:\Users\kiwamoto\Downloads\RNA_Codon_Table.csv"))
    for row in reader:
        k, v = row
        if len(k) >3:
            k = k[-3:]
        rnaDict[k] = v
    return rnaDict

def protienCoding(inputString):
    sequence = ""
    rnaDict = turnTextToLookupTable()
    for x in range(int(len(inputString)/3)):
        protienString = (inputString[x*3:(x*3)+3])
        letter = rnaDict[protienString]
        sequence = sequence + letter
    print(sequence)


    



if __name__ == '__main__':
    input = ""
    #rna = complement(input)
    #sprime =reverse(rna)
    #print(sprime)
    #crazy_rabbits_recursive(5, 3)
    #string1 = "CAATTAAGACGGCGTCGCTGCGCGGAACGGATATTGGTCTCGTTGGAGAGCGCTAGACGATTACTACCTGGTTGAACCCCCTGGGCGATTGATCTAAACTTTCGCCCTTACAGCTTTTCGGGAGTGGGCCAAGTGAGAGTGTGCTTCTTTGTCCGCGTGGAGATCTAGCTACTCTCAGTAGTCTGGACGAAGCGGGTTTAAATGGGCATTGACTCACCAGGGGTACCCTGCGGAGCGCGTTATTAATAACGTACATTAGCCAGAGTTCATGAGAGGTCCCGTCCATCAGCCATATAATCGGAGCAAACAAAGGTTGCCGTGGCGCTCAGGTCCCACATCGTCTGAAATTCAAACCCTTGAAACCACAAAGTAATCTTTTATCGACACCCCCGTATTGTTAGGTGCTGAAGGTCAGGATGCACAGCACAGCATTGCAGTAGCTGCACTGGAAAGCCTAAATTTTCCTGGTTGAATTGTTGCAGGTTACAGTTTCCGTCCTCATCACGCGGAGGATGTTGATTATTTGTAAGGTATCTCAACATTCGCTGCTAGTTGGTCCGTCTCTAATAAATGTGTGTGGTGTTAAAGCCCCCATTTATGTCTATGGAGCTCAAGGTATATTGCATGATCGTGAGCACGCTAGCTCGAATCACAACGCGTCCATATTGCCTATAGGATTACAAGAACCGTGCCCGATACGACTAAGCACAGGATGAGCGACAACCGTCCAGGGGTCCCAGCGGGCCAATCCTGTGACCGCCTCGTCTACATAGCAGTATTAAGGGTTGACATGGGCGGCTACCTGGGCGGAGAGAGCCGACAAAGAACGGACAGCGGAAGACCAGACAATGAAAGTTGTACTGCATACCGCATGACCCTGCCTTAGCCGCATGGGTTTCAAAGGTAGGCGG"
    #string2 = "GAAGAAAAATTGCCCCGACGTGCGGGTGGCATGCTCACGGAGTCCTATTGCCATCTTCTCTCTCGAGATCGATAGACGTTTCTTGTATTTGGTCTAACCTGTACCTGATGCAGCCGGGCTAGAGCGGTCCTAGTCAGGGCTTACTTGTGGGTTCGGATTGACATCCGCTGACAAACTTCAGTTTGGGAGAAGACATTTGCGATGAAAATTTGCGTACTAGATGAAGCGCCCGCAGGCAGTTATCAATAACGTGTAACATGAGCTGCTCACGTGAGTTCCTGGAAGTCACTGGCATATTAGCCGCCTAGGTCTGTCGCCGAGCCGGCAACACCAGGAATCGTCTTTACGTTCCTCGTCGAAGGACACCGATATGTCTATCTTTGCCCCACCCCTAAATTTAAGTGCTTAAGACCTTACGGTTTGAAACCGGTCTTCCGCAGCGTCTGTGGAGAGCCTTCCTTGTCTTGTTCCGAGTGTTACAATGCTGACGGAAGTGATTCCTTACCCCACGGATGTAATTGATGCGAAGGTTAGCACAATATGCTAGACCCCCCTGGTCGCCTCGTAACCCCCTGTGTGATTTCAATACTCCGATGTACGACTCTCTATCAATAAAACCTCCCTTACATGGTGCGTCCTCTAGCACAAAGCTGGTCCGGACAATAACCAGTGTATTATTACTACAACGCCGCAAGTTACGGGATGTGAGAAGGCTATCTCCGTCCATCGCGTCTTTACGAATGATCAAACCCTTGAAACGCGCATTCAAACGGCCGTTTGATCGCTTGCGGTGGTGCCGTTCATGAACGCAGAGCGTCTCACAGGAATTCACTGTGAATTAACCGACATTCTACGGGGCACGGCCTTTCGTAGGCCCCTTGCAAGGATGCATGGTTTACTATACCACCCGG"
    #hammingDist(string1, string2)
    #numPerm, array  = permutation(6)
    #np.savetxt(r"C:\Users\kiwamoto\OneDrive - Illumina, Inc\Documents\Python Scripts\foo6.csv", array, delimiter=",")   
    #thing = probabiliyDominant(27, 24, 19)
    #print(thing)
    #path = r"C:\Users\kiwamoto\Downloads\rosalind_gc (2).txt"
    #cgpercent(path)
    #turnTextToLookupTable()
    protienCoding("AUGCCACUAUUAAACUACACUCUCCUGGUAUCACGGGAUGCGUCCUCCGGGCCUUCCAUCCCGGAUAAUGUUUUAGAGGCAUGUGACUUGGGCGCACCAUGGACCUUCCAACCGGGUGCCAGACGACUAUACUACCUAUUCUCUGGAAGAUAUUCGGGGUCCAAAUCCACUCGCGUCCUUCGAAGUGGCGACAUGCCACGAAUUAACACUUGCGCGCGGCAUACGCGACGAAUUCUCCAGCCCCAUUUCUUUCUGGGGAGACCCGGGCAAGAGCCACGAAACUCUAGGUCUCCUUCCACAAGCGCCAAAAAUGAUGAAACCGGACCCCACGGUAUAGGACGUGCCUAUAGCGAGCGUCUGCGGUCUCGUCCCCCUAACGGUGAAAUCGGACAAUCAUAUCAGCCCUCGACUCAGCGGAUCUCCUUUGCGGGAUCAACACGAUGGCUGUUCGCCAAUCGCGCGCAACCGACUCUGUUUGAGGUGAGUGUGCGAGAACACGUGGGGGGGCGCUUACGGCGAACCGCUUCAGGCGUACCUCCCUACAGGGCGAUUUCGCGGACUAUGCCCCGUGCGUUUGAAAGCGCAUUGUAUCGUUUGCAGGAAACCAGACUCUAUAAGGGACGCUCAACGGGCGACUAUGCCAUUCGCCUCACACGAUAUAACGUGUGCACGAGAAGCACGCGGGGCGCAACUAAAUGGCCAUUUGCGCUCUGGGGUAUGUUAAGGCAGGUGUGUUAUGUAGCUGAUCAAGUAGUCCGGUGUUUCACAGAAGCAACUGCCGCCAUUCUCCCUCCGCGCAGGUACAUGCUUAUGCAACAUGUGGGCCGUCGAUUAGUAGAACUCCUCGUUAAGGUAUCCCUGUCUCCUCUGCUUGUUGACUCCUGCCUGUCCUGGAUAGUUAAGUGCAAUGAAGACUUCUCUCUAUGGCCCGGCCGGCUUCAUAUGCCCGGCAGUCGGGUGGAUUUACCAACCGAGGGACGUGUGUGUAUGUGGCAACAACAAUAUGGGACUGUCCCCGUGUUAUCUGAGGGGUGCAGUAACAUAAGUAACAAGGUGGGCUCUAAGCUCUCUUUAAUCUCCCCUCGGAAUCAGGCGUGUUUCUGUAGGCGAGGAAUAGUGGCUGGCUACAUAGAACAGGGACUGUUUGUCAGGCGCACCAUGGCAAGUCAUCGUAUAAUCGACUCUGUAGAUCGACAGAGAAAUGAAGUUACCUCGCAUUGCACUAUACGGGUAACCAGUAAUGUCCAUUUUAGGGCGUGUUUACCCUGCCGCGCGAUUAUAUAUUCUCCUCCCAGUACUGAAGAGAGACAUGUACUUCAAAUGGACCCUCUUACCCCUAACCGGGUUCUGAUUGAAAAAAUAUCCGGGUCAAAGACGACCAGCACCAUGCCCAGCGACUGUCCUUCGAGUUCACGGCACCCGAGGAGCCCGACGCGGGGCCACGCGCCGCGAUGGUAUCAGACCAUUAGUCAAAUUGGAGACAAUAGUCCAAAUACAGAAGGACGUUACAGGCAGGGGGUUCGAAUUAAGGGCCGCGUGCCCGCUGGGGUCUGGGAUCUCGGAGGAAAGCACCUUUAUCGGCCGACUAACAAAAUUUGGCACGUUCGAUCCACGUUGAUGCCGCUCCGUUCCCUCGGACUCGACGCGGUGUCAAGUAUCUACGUACACGUUUGCGUCCUUAGAGUGUCGAAGUUACAAAUGCCACUAGAAUUCGGCUGUUCGCCACGUUUCUCCAUCCCUAAACUGAAAUCCCAAACAUUGCCGCCGCUGGUUACACCAAAGACAUCUCUUGCCGAAUUGGGCUAUCAAGCAGCAAAAUGUCCAGUGACGAGGUUCCUUCCACCCUUGGUAUAUGGCAAAGCCCGGUACGUCCGGAAUCAGACCUACUUUGUUCAAAAAUCUGAGCCCUACGAGGCUCGGUUAGGAGCUGAAGGCUCGAUGGUCGGCCUUAAUGGUCACAGGGUGAGGGAAGCUGCAAGCACCGCCCCAUUGUAUCGAUCGCAAACGGAAUCUCGGGGGAAAUGGGCCCCAGGGUCCAAACCAAAAGACUGUACUAAAUCUCUAGUAGUGAGGCUCUACUCCCGCGAGGCCACGCCUCGGGACCAUUCCGCGUUCUUGGAGGAUAUACUCUCCAGGCCGAUAAGGUACUGCACUGCGAACCACGUUACUGAGCUCCACGUCGGGCUCCGAAUUUUCAGGGGCCUUGGUACGUGUGCAUAUUACUCAGUUCCGUGUCUCCUGAGUCCAAACCAAGCAGUAUAUUGGCCGAAAAUGGGGGCUUACGGAGCGUCGCCGUGUGAUGCCACUCAAAUAGACGAACGCCCGGCUAGUAAAGUUCUACGUCCAUCAUUUGUGACGCUGCUAUCUCGCAAUACUGAUCUAAUGUGUCAUGAGCCCAUGAAACUAUGCUCCGUAGUACAUGCCUCUAGAGUUAUUACAAUGAAGAGAUUCAGAACCUUCUCCCUGCCCGGUCUGUUCCGAGACGGGUUAAAUACUAUACUGAUCCAGUACGGAUUACAGCGUCGAGGCCCGAAAUUAGAGGUUACGUCGUCAAAGAGGAUAGCUCCUGUGUUCGGCAUGGCGACAGGGUCUCCAUUCCGACGGCGAUCGACCGAGCCUGCCGGUCGCUUCAUCUUAAGCGUCUGCUGUCUUGAUACUCCAUAUACGUUGAUUAUGGCAUCUCGUGAUGCGGCUCACCGACGCGUUAGUUCAAAAGGACGGAUCUCUAGUAGUGGGAACGAAACCGGCUCAAUGGUCCAGUUAACGGCGCAGAAUCUUCAAAAGUGUCGCCAUCCCGUAGCGUUAGAAAGCCCGAACAAACGAUUGCUGUACGAGCGAGAGACCUCCGGCCUGUCACGCACUGGUUCCCCCGGGACACCAAUUCCCAUCUCAAUUUAUACGGGGGGAGAACAAUCGUCACAGGGGGACCGCUUACGAAACGCUGACUGUAGCAUUACACGGAUAAGAUUAAAAUAUAGCCCAUUGGCGCGGCGCAACUUGGAGCAUCACAAUGCCACGCCCCGUUGCCCUGUAACUUAUAGUCAGUACUUUAAAUCAGUUCUAUACAUAGCCAUGGGGGCCCUUUUGAAGAAAUUUUUCAUUGAGCCGGGGGGCAUCAUUGUAAUAUUUCACAUGGGCAUUGUAGGUCCUGGCUGCAUGAAAUGCAGUUUCUCGUUCGGGCCACUAUUUCUAAAACGGGUAUUCGGGUAUGUGACUCAUCGGCGCACGACCUCGGCGCGCCGUCAUCCGCCUGAUUCCCGGUAUUAUACACGAGCGGCGUCAUGGGCUGAAGCAAGAUGCGCGAGGCUAUCAGCUUACUCAUCUUUCCGCAAUGUUUUUUAUGGCAUCGUUCCUGCUCGCCCCGCUUUAGCGAUCGUAGGUGCCAUUAAAGUCAAGUGCAUCCCUUACGCCAGGCACGAGACGACCAACUCUAAUGUCCUUAGAAUGCAUUGCAAAGCAUUGCUUACCGUACGUCCUCCGUGUUGUCAGUGCAUCGGCCGUACCGCGCGUCGAACGAAACGCGCAAAAUUCCCGCUUACAACUUACAUUUUAGGUGCACACCGACAGGACACUCUUGGACCCCGGGGCGAGUCCACAGCCGCUCUACCUUGGAAUUCGAGAUCGGACAACCGUACUAUCGAGGUGUUCCCCUGCGUAAGACAACACCAAGUCAGAUACAAAGGAAAGCCCUUACUGAUCCUUUACAGGAUCCGGAAAAACCAACGUGAUAAUUCUGACUUCGAGCGUCAGGAGUUUACGACCACAAAGUCCCAAUACCUACCUAUGCCACAUAUCAUGGCAGGCAACGGGCUUGCACCAAAUCAUACAGUUGACAGAGGUGGUCCAGGCAGCAGAUCAGUAGAUCAUAUUCUCCCCUCGUCCGGGCUUCGUUACGAACCAAUGCAAACGUACUCAAUUCCGGAGCGAGAUUUACCCGUCAGCGCCCUGCGCUUUUCUGGGCUAAGACAACUUCGCGUCUUGGCGCAGAGCGCUAGACGCCGCAAUACACUGCGCCCAAAACCCGAACCGCCGUCCGUCUUCGCGAAGGCGACCGUAGCUCCCAGUAGAGAUCAAAACCGUUACCGUCCACAUCCUCUUCACCCGUAUGUAGCUAGAUUAGAGCGCACAUGUUUCCGGACUCAGCGCUCGGCCCUGGUCAGACACUGGUCCCUGUUGGCUCACCGCAUAGAGAGGUUCACAGUGGAAACACCUGGCUUAGGAGAGUCCCUGUCUAACGGUGUCACUCGAAGAAGUCUGCCAACCGACUUGGCUACAAUUAAGUGCUCUAGACCCGUAUUUCGGACGGGACAGACCCACGGUAAUGGGAUAAACUCGUGCUCGCCGACUUUAGUGUUAUUGGGGUUCUCGGUACUAGGUCCCCAUCUCUAUAGAGGCCACUAUCCCGCUAUUUCUCACGAACAUCUAUUGGGAAGUCUAAGUUGCCGAUUGUCAGAUACAAGACGUCCGUCGCAAGGGGUCCUUUCCGUAGCAGCGCAGUGGAGGUACCCUGUUUCAUUCAUACGUCGAGGGCCGACUGUCUUCAAUAGAACUUGUGAACUAAUGACCGGAUACCCUCAUAACUACCUCUCCGACCUGAAAAAGGAACGAGUGUUAUAUCACGAUCGGAUGCGAUGUCAAUUUGGUUCAUUGUGUCAUUUGGAAGGUCCGUCUACUUCCGUGGACUGUCAACGAGUGCCAAAUCUUCUGUCUACACACUUAAUGCGAGGAGCAUUAGGGCAGUUAUAUCUGCACUCUGAAAGAGUUACGCGCUUAACAUUGGAACCAUUAAUACCGAAUAGUCCUCCUGUCUCUGAUGACUGGCUCGGCUUGCUAGUAAUACAGGGAUGCGCACAUAUCCAAAUUGUAAGAAAGAUCAUGACGAUCUAUGUGGCGCGUAAGAUUAUUUGGCGCCCAUGGUACGCGUCCGCCUGCCCAAAACUAGUACACUUCACCAAAGCCAGUCAGUCACUGUGCGUCAUACUGUGUAGUGCCAAUCCGCCCUACAAUGGUCCGAAAUGUCGGGCUAUCAAGGGUAAUGUAUUGUUGGGAUUUAGGCUGUCAUGUCACUGCGAACAGCUAGUUUAUGCCGCUGAGCAUGGUGACCGCCAUGGACUAUACCAUAACCAUAUAGCUGACCCCUACGUUCGCCUUCAUGAAGGGCCGUCCCAGACAUGGCCAUACAAAAUUCCGACGAUCAAGGCGAAGAAGUUUAUAGGAGUGGCAAACGCAGUAACAACCGCAUGUGUGGUCAUACCCAUACAUGCGACGCGAGGGUCAUUUAGGGGGAUAGGCAGCAAUAUAUAUAUGUUGAGUUUGGAGACAUGCUGUAAUAAAUACACGUACAACAGGACGCAGGAACUUGGCGUGCUGAGCCUAAAGGCCCUUGUUGUCAACUGCUCCAGGGCAAUAUUGAUGUCUCGCUAUAUAUGUGCCUUCACUUCGCAGGCGCUCCUUGAAGCGACAAGCCUUAUAGGUCGGGCAUUAGCCAUAUCAUGGGUGGUCAGUUGGGCGGGGGAGCGGCGUACUUAUAAGUAUUGCGAGUGCUCAGAAUCGCAAGUUAUGCGGGAGCAUGGCUUAAUAGGGUUCGCUAGCUAUCUAAAGGAUGAUUACUUAAACCCAAGAGAACACAGUGGGGGGCGCCGAUGUUCAAUUGGGGAGGUCUGUCCAGAGGAACACUGUGGCCGUUCAUGCGACUUGUGCAAACCAAAGUCCGAAGACAUCCACGAACGAUUUUCACCUUGUCAACUUACCCGCGGCUUAGCAAACAAACUCGCUGUUUGCAACACUCCGGCUCGGACGGCACUCUGCGAUUUUUCUCAGGCCGGCAACGGAAUCCCUCGCACCUUCCCUCGCCGUUGCUGCGUAAUGCUAGCCAAGUGUAAUCGGGGCCCCUCGUCAAAACGAUCUGGGCUUUCAAGAAACGAGAGUGCCAGCUGGGGAUACUUAGGCUACUGUCACUCCCCCGAUUUGCCAGACCCAAUGUGGGAUUCUGGUACGUACUGGGGGUCGCCAAUGGCAACUGCGAAUCCGCUAGACGUCCAAGCAGGACCCCCCAAGCCGUCGAAAAACCUUUUACUUGUAGACUACGUAUCGGGCACGUAUCUGCCAGAUCUACAAAACAAAGGCUAUCCCGCACUCCGCAGGCCGGACGACUGCCAGACUCGUUCUAGUACGGUACUACUUACGGUGAGAGGUGCUAGGUGGUUAACGUGCCGCAACAAGUUCGACCUGCGGCUAACUUGUCUAGGACACAAAUUAAUCACCUACUCUAGUGUGCUGUGCGACCAGAAGGAUAUGCACUUUCGAGCUUAUCUAUACAUCUUCACGCGUAAACAAAAAGGGUCGGCAGAAAUAUUAUCUGGCCCAUCCGACCCAAGGCUACAGGGCCGUGAGUCAUACUUUGUAGCCCGGAUCAUCUGGUACGUCGAGUUCAUUGUCCCGCUCAUAGAGUCACAGACGACACAGCAGCUGGCAGCCGUAUGUAGGUCAGGUGCUUUGCUCCAGAACUUGUCCGGCCAUACAGGUCUAGGUUUCUCUCGUGAAUAUGGUAAGACCCGAGCCAUACGUUCUAACCGAGUAUGUAUGUACCGGAACUCGAGCUGGCGGGCAGCCACCGGUACAUGUUGGAUAACCAAGUCCCAUUCGGCGCAUUACGGCCUUCUUGGAUAUUUGCUGAUACAAGUGAUUCACACGCCAAUGUCCGUGACCUUGCUCAUUAUCGAUGAUGGUCAGCGGUUAAUCUCAUGUGCAUGGAGCAAAAGAAUGGCGCAGUCGCUUCACACUAUCGAUCAAUACCCGUUAUUGAGCAAUAGAGCUUCUGGGGAAAAACAGCUGUCAGCAACGGGAAUGAUUCAUGGCCUCGGCACUGACCUCUCUUGCACGGGGCGCUUUUUGAGCCCGGCUUCGUAUUACUCUAUGCGCACUCAUUAUUUACCAGCUGAGGCACCUACAUGUCCUCCUUCAUCCGGGAAUCCCUGGACUGACAGGCGCACGAGUGGUAGUUUCCCUGCGCGUAGCCGGCGAACCGUAGCCGCAUUGCAAAGGAGACUCCGCCCAGAGUUAAACACAGAACACCUAGGGCACUGUCUAAGUGCAGAAAGGGCGCGAAGUCUGUGGGCAUAUCUUUUCCGGGUCGUAGGACCGCCGUCUUUAUGGCCGACCUACAUGGCUAACGGCGACAUCACACGCUUGUGCCCAUUUGAAAGUUUCGUGCUUAAUCCUAAGGCGAUAACAAUUCGAGCGGCCGGAACUACUAAUCUGCGUAAAUGUGUUCAUGGCCUUCGUAUUUGGUUGAAUUUCUUAGGUGGUGGAGUUGCGAUGCGGCGCCCCACAAAUAUUCAAUGCAUCUACAGAACUAGCACUAAUCGGCGAGCAAGCUUGCAAGCACGAUGUCAAACUGCUCAUUUUGCAGCUCUAGCGUGGACGCUACCAAGAAAACUCAGCAGGAUGCUAGUGACAGGGGUCUACCUUCUUCGAAAAGAGAUUAAACGCCCCGGAUUCAGGGAUCGACCGCGCGAGCCAGGUUCCACGGCAGCCUUGUUGGUCAGCUCGGCAUAUCAAGUCCUCGCUGUCUCUCCUGACAGGCGCAUCUCGUUAUCCUCUGGCCCGAUAGCAACGUUGAGAAGACCCUGCUGCGCGACACUCAGUUCAAUGACGACGGAAUAUCGGCGCGGAUACUUCGCCCUAGGCAGCACUAACUCGGGAACAUGGACAUUGUACCUUGCGUCACAUAAUUACGCAUUCCAGGCGGAAAUAUAUCGCAUCUAUCGUCCAGUAAUCAGCACAAUAGUUCUACAUAAGAAAAUGUCGAAUCGUCCAGGGAUAGUUAGCCGAUCGUGCGCGGCUCUUUUACGACCCUCGCUUGGAGUGCUACUUCUGCGGGCUAAUCGCGUCAACUACACGGACGAAGUUUAUAUUUACUGCACUCCCCGAUGCUGCACCCGCUGCUAUUCAAUCUUAGUCUCCAACCUUUUCGGAAAGUUCGACGUGCCCUUUACUGGAGAGGGGAUCAGGUCUCGUAGGAAGUCUACGCAAUUUGAUGUCGUAUCUGUCAAACGUGGGUUGGGCACGCGACAACUGCCUGGAUACGGCCACGGCAGAAUCGGGAUUAGUGGCGUAACUGCUGUACCGACAGCUUCUCAUCUUACGAGACUAAUCCGUCGGUCCACCAGGCUUCCGGAAACCGACUUUCAAAAUCGGGACCGAAACGCCGCCGUGUAUAAAUUUUGGGAUGGUGGACCGGAGGCUGGUAUAAAGGGGCCAAUCAGGAGCAACGGUGCUCAAAGACUCGUUGUUCUUUACCUACUUUAUGGGUACUACAGGCAGUUCUGCUACAGAUCCUGCAACUGUGUACAACCCGCCGCCCAAACCAACAAAUGGUUGAGUGGUUUUACACGAAGUGAAGCAGGAGAACGGGGCUGGUACUGCAGUUGCACAGUGCUUGCCGCGUCGCGCUCCGGCUGUAGUCUGUGGUUACACUCAAAAGCUGCAGGGCAUUCCCCUCUGAUGGCUUACAUUCCAGGCCCUGUGAUGAGAUCAGUUGUGCCGGAGUAA")