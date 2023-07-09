import random as ram
from collections import deque

i = 0
m = 0
n = 0

while i < 5:
    print("Throw number "+str(i+1)+":")
    listCurrentThrows = deque(maxlen=10000)
    currentQuantityOfSixs = 0
    currentQuantityOfFour = 0
    for j in range(10000):
        upperFace = ram.randint(1,6)
        if upperFace == 6:
            currentQuantityOfSixs += 1
        listCurrentThrows.append(upperFace)
    
    listOfSelectedIndexes = deque(maxlen=1000)
    for j in range(1000):
        randomIndex = ram.randint(0, 999)
        if(not(randomIndex in listOfSelectedIndexes)):
            listOfSelectedIndexes.append(randomIndex)
            if(listCurrentThrows[j] == 4):
                currentQuantityOfFour += 1
    
    print("Average number of times we get six "+str(currentQuantityOfSixs/10000) + " of the 10,000 throws.")
    print("Average number of times we get four "+str(currentQuantityOfFour/1000) + " of the 1,000 throws.")
    print('---------------------------------------')
    m += currentQuantityOfSixs/10000
    n += currentQuantityOfFour/1000
    i += 1
    
print("Value of M "+str(m/5))
print("Value of N "+str(n/5))

    