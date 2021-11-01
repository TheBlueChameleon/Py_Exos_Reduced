# FWest
#
# Problem 4-4
# In more or less linear time (Christians estimate)

# Note: To match N socks, this code will take ~ N*log(N) units of time.
# This is because of how Python's sorting algorithm ("Timsort") is implemented.
# If you want a more detailled analysis...
# * you could attend Algorithmen und Datenstrukturen, where sorting algorithms
#   are discussed in much detail
# * look up MergeSort and Quicksort (the two algorithms upon which Timsort is
#   based)
# * look up the Master Theorem, which gives an estimate for the runtime of
#   recursive algorithms such as Timsort

### IMPORTS
import random
import time
### VARIABLES

socks = [i for i in range(1000000)]*2
random.shuffle(socks)

### FUNCTIONS

def matchSocks_faster(socks): # seems to scale with N
    pairs = [(x,y) for x,y in enumerate(socks)]   #Ich mach ein Tupel (Position, Paarnummer)
    revPairs = []
    for pair in pairs:        # Daraus werden die Tupel (Paarnummer, Position)
        revPairs.append((pair[1], pair[0]))

    # note: instead of creating a second list revPairs, one could directly swap
    # positions in the definition of pairs:

    # pairs = [(y,x) for x,y in enumerate(socks)]

    revPairs.sort()    # Das wird sortiert, haette auch einfach nach dem zweiten Element sortieren koennen
    matches = [0]*len(socks)
    for i in range(0, len(socks),2):     # An der Stelle vom ersten Socken wird die Position vom zweiten eingefuegt
        matches[revPairs[i][1]] = revPairs[i+1][1]
        matches[revPairs[i+1][1]] = revPairs[i][1]
    return matches

### MAIN

starttime = time.time()
#print(socks)
print(matchSocks_faster(socks))
print(time.time()-starttime,"s")
