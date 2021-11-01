# ============================================================================ #
# problem 4

print("MATCHMAKING")

# For this problem, let's assume it is very time consuming to compare two given
# socks with each other. Most steps take virtually no time, but deciding whether
# or not two socks form a pair should take considerable time.

# This assumption could mirror a real world scenario when, for example, socks
# are identified by strings: whether or not two texts are equal can only be
# decided after comparing *all of their characters*. So, when comparing a lot of
# "socks", we do a whole lot of work which will take time and give a less 
# performant algorithm.

# Below, you'll see an easy to understand but slow algorithm and a more 
# sophisticated, recursive algorithm. To really understand the recursive 
# approach, revisit the code after day 4 of our course.
# The recursive approach makes it much faster to go through the socks, as is 
# shown in the output of the code.

# If you enjoy such considerations, please do consider taking the course
# Algorithmen und Datenstrukturen by Prof. Solbrig in the summer term!


import random         # already imported from task 2, but importing it a second time does precisely nothing

# ---------------------------------------------------------------------------- #

def makeSocksList(P) :
  # argument P is the number of *pairs*, i.e. number of socks N = 2*P.
  
  reVal = []
  for i in range(P) :
    reVal += [i, i]    #  [chr(i + 65), chr(i + 65)]    # chr(a): create a character with ASCII code a
  
  random.shuffle(reVal)
  
  return reVal

# ---------------------------------------------------------------------------- #
# simple algorithm, taking (on average) N * (N-1) / 4 steps

def directApproach(socks) :
  N = len(socks)
  reVal = [-1] * N              # Initialize with "meaningless" value -1. This allows to later easily see whether our algorithm works or whether it skips socks.
  comparisons = 0               # Count, how many comparison steps are necessary -- only for comparing to the other approach
  
  for   i in range(N - 1) :     # Sequentially, take each sock in the heap except for the last one in the "left hand"...
    for j in range(i + 1, N) :  # ... and, aequentially, take all socks in the "right hand" that weren't in the "left hand" before
      comparisons += 1
      if socks[i] == socks[j] : # compare left hand (index i) and right hand (index j)
        reVal[i] = j
        reVal[j] = i
        break                   # save some time: if a sock and their partner have been found, the search needs not to be continued.
      
  return reVal, comparisons

# ---------------------------------------------------------------------------- #
# advanced recursive approach

def recursiveApproach(socks) :
  # outer function only gives a more convenient interface: only socks go in
  
  if len(socks) < 2 :
    raise Exception("Cannot form pairs!")
  
  comparisons = 0             # again: count comparisons for efficiency analysis
  
  # The inner function does the true work. For the end user there are 
  # superfluous parameters start and length which are thus hidden.
  
  # Compare socks in the sub-heaps with indices [start : start + length]
  
  def matchSocksRecursive(socks, start, length) :
    nonlocal comparisons      # we'll cover this on day 4: 
                              # use the variable defined in the outer function
                              # rather then have it local to the inner function
    
    matches = [-1] * length
    
    # are there only two socks? Compare them immediately
    if length == 2 :
      comparisons += 1
      if socks[start] == socks[start + 1] :
        return [start + 1,  start]
      
      else :
        return [-1, -1]         # negative indices indicate: socks were not matched
    
    elif length == 1 :          # only one sock -- no comparison possible
      return [-1]
    
    # from here on it is clear that the heap of socks is bigger than two.
    
    # split the heap into a left and right half
    lengthLeft  = length // 2
    lengthRight = length - lengthLeft
    midPoint    = start + lengthLeft
    
    # Recursion: think not only of the code above, but also keep track of what
    # is written below this.
    # We assume that matchRecursive returns a list of numbers. These lists are
    # exactly as long as indicated by the third aprameter, length.
    # The numbers are either non-negative (if a match could be found in the
    # sub-heap [start : start + length]) or -1 if no match has been found yet.
    # We now need to find the counterpart of the unmatched socks in the left
    # heap amongst the unmatched socks in the right heap.
    
    matchesLeft  = matchSocksRecursive(socks, start   , lengthLeft )
    matchesRight = matchSocksRecursive(socks, midPoint, lengthRight)
    
    for i, match in enumerate(matchesLeft) :
      if match >= 0 : continue      # sock has been matched before -- skip
      
      for j, candidate in enumerate(matchesRight) :
        if candidate >= 0 : continue
      
        comparisons += 1
        if socks[start + i] == socks[midPoint + j] :
          matchesLeft [i] = midPoint + j
          matchesRight[j] = start    + i
    
    return matchesLeft + matchesRight
  
  return matchSocksRecursive(socks, 0, len(socks)), comparisons
  

# ---------------------------------------------------------------------------- #

P = 26             # numer of pairs of socks
N = 2 * P          # number of socks

socks = makeSocksList(P)
matchesDirect, stepsDirect = directApproach(socks)
matchesRecursive, stepsRecursive = recursiveApproach(socks)

correct = all(socks[i] == socks[matchesDirect[i]] for i in range(N))

print(   "Index | Socks  | Matches Direct | Matches Rekursive")
for i in range(N) :
  print(f"{i:4}  | {socks[i]:^6} | {matchesDirect[i]:8}       | {matchesRecursive[i]:8}")
print()

print("steps taken in direct approach   :", stepsDirect)
print("steps taken in recursive approach:", stepsRecursive)
print()

print("both approaches yield the same:", "Yes" if matchesDirect == matchesRecursive else "No")
print("solutions correct             :", "Yes" if correct                           else "No")
print("recursion was faster          :", "Yes" if   stepsDirect  >   stepsRecursive else "No")
print()
