# Question 1

def getMaximumOutfits(outfits, money):
    last_outfit = len(outfits) - 1
    max_outfits = 0
    for i in range(0, len(outfits)):
        remaining_money = money
        j = i
        while j <= last_outfit and remaining_money >= outfits[j]:
            remaining_money -= outfits[j]
            j += 1
        if (j - i) > max_outfits:
            max_outfits = j - i
    return max_outfits

# Question 2

import numpy as np
def numDuplicates(name, price, weight):
    arr = np.array([name, price, weight])
    arr2 = [tuple(row) for row in arr]
    return len(name) - len(np.unique(arr2, axis=1)[0])


