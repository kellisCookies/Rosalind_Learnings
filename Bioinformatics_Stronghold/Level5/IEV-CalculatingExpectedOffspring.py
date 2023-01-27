import numpy as np

Dompercent = np.array([1, 1, 1, .75, .5, 0])
numberOfOffspring = np.array([16990, 16930, 17015, 19904, 16880, 17459])

expectedNum = np.multiply(Dompercent,numberOfOffspring*2)
sum = expectedNum.sum()
print(sum)