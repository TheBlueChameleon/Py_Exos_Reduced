# ============================================================================ #
# problem 1

print("### Chain Generator")

def chainGenerator (*elements, sep="-") :
  result = ""
  for e in elements[:-1] :          # list[start:stop] goes up to and *excluding* index stop. -1 is the index of the last element.
    result += str(e)
    result += sep
  result += str(elements[-1])       # append the last element explicitly, do not append the separator string

  # or, all in one line:
  result = sep.join( str(e) for e in elements )

  return result

print( chainGenerator(1, 2, 3) )                  # Ausgabe: 1-2-3
print( chainGenerator(1, 2, 3, 4, sep="~~~") )    # Ausgabe: 1~~~2~~~3~~~4
print()


# ============================================================================ #
# problem 2

print("### Sort by vector length")
data = [(9, 1), (8, 2), (7, 3), (6, 4), (5, 5)]

print( sorted(data, key=lambda x: x[0]**2 + x[1]**2) )
print()


# ============================================================================ #
# problem 3

print("### Binary Search")

def binarySearch (data, searchTerm) :
  print(data)             # this is only to show how the list is broken down -- remove for "pure solution"
  size = len(data)
  
  if (size == 1) :
    if data[0] == searchTerm : return True
    else                     : return False
    
  else :
    midPoint = size // 2
    if   data[midPoint] == searchTerm : return True
    elif data[midPoint]  < searchTerm : return binarySearch(data[midPoint:], searchTerm)
    else                              : return binarySearch(data[:midPoint], searchTerm)

data = [1, 5, 6, 7, 8, 42, 96, 666, 1337, 2112]
searchTerm = 42

print(binarySearch(data, searchTerm) , end="\n\n")      # test for middle element
print(binarySearch(data, 1)          , end="\n\n")      # test for first element
print(binarySearch(data, 2112)       , end="\n\n")      # test for last element
print(binarySearch(data, 2)          , end="\n\n")      # test for not in list


# Runtime analysis:
# The shown iterative version of the search code "touches" each element of the
# list data in sequence.
# Best case scenario: the search term is the first element --> 1 operation
# Worst case scenario: the search term is the last element --> N operations
# On average, the search term will be in the middle of the list 
#    --> N/2 operations
#    (assuming the element is in the list at all. If we assume this holds only 
#    half of the time, we need to touch all N elements half of the time, and the
#    otherhalf of the time we finish after N/2 operations, giving a grand total
#    of 3/4 N operations.
# 
# The recursive algorithm, on the other hand, doesn't touch *all* elements, but
# only specific ones. Since in each recursion step the list is halved, and the
# algorithm terminates once the resulting sublist has a length of one, we know
# that the number of operations is the number of times we can cut our list into
# two and still have something left. In other words: we need log_2(N) operations
# 
# For big N (think N=1024 or more), this makes a HUGE difference. For example,
# the iterative approach would need (on average) 768 operations, while the
# recursive one has found an answer after a mere 10 operations -- almost two
# orders of magnitude faster!
# 
# Of course, this comes at the price of a condition: the recursive algorithm
# works only for pre-sorted lists. Sorting a list can be rather time consuming;
# most good algorithms take something on the order of N*log(N) operations to do
# this, essentially eating up the advantage.
# However, you only need to sort once. If you have a sorted list and need to 
# find values over and over, this algorithm does make sense!

# ============================================================================ #
# problem 4

print("### antiderivative")

import math

def antiderivative(func, N = 1000) :
  def integrate(stop) :
    result = 0
    width  = stop / N

    for i in range(N) :
      x = i * width
      result += func(x) * width

    return result
  return integrate

theCos = antiderivative(math.sin)

# pseudo-graphical representation:

for x in range(20) :
  print( int(theCos(x / 3) * 10 + 20) * " ", "*")
print()

# This solution is horrible when it comes to efficiency, but the aim of this
# is going through ideas of scope/visibility/data flux.
# Consider taking the lectures Numerial Recipies (Solbrig, Winter Terms, focus
# on coding aspects) or Numerics (various lecturers, Winter Terms, focus on
# maths) if you're more interested
