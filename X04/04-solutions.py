# ============================================================================ #
# Problem 1

vector_a = [ 3, 2, 1, 5, 7, 2, -1]
vector_b = [-7, 3, 7, 5, 6, 8,  1]

# version 1: index based
result = 0
for i in range(len(vector_a)) :
  result += vector_a[i] * vector_b[i]
print(result)

# version 2: using zip
result = 0
for x, y in zip(vector_a, vector_b) :
  result += x * y
print(result)

# ============================================================================ #
# Problem 2

text = "the quick brown fox jumps over the lazy dog"
uniqueChars = set(text)
sortedChars = sorted(uniqueChars)

# automatic version
autoCounts = {char : text.count(char) for char in uniqueChars}

# manual version
counts = {char : 0 for char in uniqueChars}       # initialize dict with start values 0

# alternatively:
#counts = dict()
#for char in uniqueChars :
#  counts[char] = 0

for char in text :                                # count manually
  counts[char] += 1

print("Analysis of '" + text + "':")
for char in sortedChars :
  print(char, "appears", counts[char], "times; automatic count yields:", autoCounts[char])

# ============================================================================ #
# Problem 3

# ---------------------------------------------------------------------------- #
# Approach 1

height = 7

for row in range(height) :
  print(" " * (height - row - 1), "*" * (2 * row + 1))
print()

# ---------------------------------------------------------------------------- #
# Approach 2


for row in range(height) :
  for column in range(height - row) : print(" ", end="")
  for column in range(2 * row + 1)  : print("*", end="")

  print("")

# ---------------------------------------------------------------------------- #
# Approach 3

for   row    in range(    height    ) :
  for column in range(2 * height + 1) :
    starFlag = abs(column - height) < (row + 1)

    print("*" if starFlag else " ", end="")
  print("")

# ---------------------------------------------------------------------------- #
# Approach 4

width = 2 * height + 1
for i in range(height * width) :
    row = i / width
    col = i % width

    if ((col <= height - row) or (col >= height + row)) : print(" ", end="")
    else                                                : print("*", end="")

    if (col == width - 1) : print("")

# ---------------------------------------------------------------------------- #
# Approach 4

formatstring = "{" + f":^{2 * height + 1}" + "}"

print(formatstring)

for n in range(height) :
    stars = "*" * (2 * n + 1)
    print( formatstring.format(stars) )

# ============================================================================ #
# Problem 4

# Depending on the chosen approach you'll find two (possibly even more...)
# different yet *correct* results. There are multiple ways to break a rod that
# influence the resulting probability.
# Here, we don't want to go too deep into the subtleties of stochastics but
# focus on the coding techniques.

# Basic idea:
# To form a triangle, the condition has to be satisfied: The longest piece
# has to be shorter than the other two combined.
# This is equivalent to:
# The longest piece must be shorter than half the entire rod

# ---------------------------------------------------------------------------- #
# Approach 1
# Pick three lengths a, b, c, as recommended on the problem paper.
# I.e. we first break a piece a of random length off the whole rod (length 1).
# After that, we break off a piece b of random length of the remainder of the
# rod (length 1-a).
# What is left then gives piece c = 1 - (a+b)
# Result: ca 0.193

import random

hits =    0
N    = 5000

for n in range(N) :
  a = random.uniform(0, 1)
  b = random.uniform(0, 1 - a)
  c = 1 - (a+b)

  lengths = sorted([a, b, c])

  if lengths[0] + lengths[1] > lengths[2] :
    hits += 1

print(hits / N)

# ---------------------------------------------------------------------------- #
# Approach 2
# Pick two *points* x, y at which the rod is broken. From this, compute the
# lengths.
# Since point y may be located before x, we get a hidden additional choice after
# breaking the off the first piece: either we break piece b off the remainder
# (lenght 1-a, as before), or we break b off of a. This is why there are two
# different yet corret results.
# Result: ca. 0.25

hits = 0
for n in range(N) :
  x = random.uniform(0, 1)
  y = random.uniform(0, 1)

  x, y = sorted([x, y])

  a = x
  b = y - x
  c = 1 - y

  lengths = sorted([a, b, c])

  if lengths[0] + lengths[1] > lengths[2] :
    hits += 1

print(hits / N)
