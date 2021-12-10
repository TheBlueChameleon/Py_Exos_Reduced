# The fastest solution to the sock matching problem I've seen so far.
# Thanks for Johannes Zander for submitting this solution.
# The algorithm uses extra memory to save on comparisons. This algorithm goes
#   through the list of socks exactly once.

# ============================================================================ #

import random

# ============================================================================ #

def makeSocksList(P) :
  reVal = []
  for i in range(P) :
    reVal += [i, i]

  random.shuffle(reVal)

  return reVal

# ---------------------------------------------------------------------------- #

n = 5
socks = makeSocksList(n)

index = [-1] * n
matches = [None] * n * 2

for i, sock in enumerate(socks):
    if (index[sock] < 0):
        index[sock] = i
    else:
        matches[i] = index[sock]
        matches[index[sock]] = i

print("socks:  ", socks)
print("matches:", matches)
