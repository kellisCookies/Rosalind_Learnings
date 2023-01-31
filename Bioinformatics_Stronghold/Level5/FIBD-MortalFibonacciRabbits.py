import numpy as np
"""
the concept is to have bins from 1 to months alive to show all the bunnies that are in the population
any bunnies older than monthsalive should not be counted



example:
                            bunny age 
                0       1       2       3     Total  (month 3 bunnies contributed to a baby at 0 but have passed and dont count in total)
month 1:        1       0       0       0       1
month 2:        0       1       0       0       1
month 3:        1       0       1       0       2
month 4:        1       1       0       1       2
month 5:        1       1       1       0       3
month 6:        2       1       1       1       4        
"""
def mortalbunnies(nMonths, monthsAlive):

    generations = [0]*(monthsAlive+1)
    generations[0] = 1

    for n in range(1, nMonths): #for each month, increase the index of months, sum the babies made, then output the total
        #print("adding a month" + str(n))
        generations = generations[:-1]    
        #print("making babies")
        babiesMade = sum(generations[1:])
        generations.insert(0,babiesMade)    
        
    print("total Bunnies:" + str(sum(generations[0:monthsAlive])))


mortalbunnies(80, 20)

