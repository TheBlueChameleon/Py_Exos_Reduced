# ============================================================================ #
# Problem 1

# factorial returns n! = n * (n-1) * (n-2) * ... where n is an integer
# radians converts degrees (0..360°) to radians (0..2pi)
# index searches an element in a list and returns the index of the element IF it
#   can be found. Otherwise, a ValueError is triggered (this will be covered 
#   later in detail. In brief: program execution is aborted with an error 
#   message)
# pop retuns and deletes the last element of a list, if called with no argument.
#   if an argument is provided, it must be an integer and specifies the index of
#   the element to delete and return
# clear deletes all objects in a list

# This can be illustrated as follows

import math

myList = ["Dusky", "Joe", "Hartington"]

print("### ELEMENTS IN MODULE MATH:")
print(dir(math))
print()

print("### ELEMENTS IN CLASS LIST:")
print(dir(myList))

print( math.factorial(4) )       # Output 24 = 4 * 3 * 2 * 1
print( math.radians(180) )       # Output 3.141592653589793 (also pi)

print( myList.index("Joe") )     # Output 1 (Index of 'Joe')
#print(myList.index("nobody"))   # triggers an error message

print( myList.pop() )            # Output: Hartington
print( myList )                  # Output: ['Dusky', 'Joe']
print( myList.pop(0) )           # Output: Dusky
print( myList )                  # Output: ['Joe']

myList.clear()
print(myList)                    # Output [] -- myList is still a list!


# ============================================================================ #
# Problem 2

stringVar = "My Hovercraft is full of eels"
everySecond = stringVar[1::2]
wordsInList = stringVar.split()

print(everySecond)
print(wordsInList)

# ============================================================================ #
# Problem 3

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

print(matrix[0])
print(matrix[1])
print(matrix[2])

matrix[2][0] = -7               # Change row 3, column 1

# ============================================================================ #
# Problem 4

book = [["Peter", 19, 1.80], ["Jasmin", 20, 1.63], ["Alex", 22, 1.93]]
book.sort()

print(book)

# Currently, to change the sorting criterion you can only do this by changing 
# the order in which the list elements are arranged. I.e. put the age before the
# names:
# book = [[19, "Peter", 1.80], [20, "Jasmin", 1.63], [22, "Alex", 1.93]]

# ============================================================================ #
# Problem 5

print( list("ab" * 9) )

# ============================================================================ #
# Problem 6

# The multiplication does not duplicate the content of the list, but only the
# references to these contents. So you could imagine the line
#   A = [[1,2,3]] * 3
# to decompose into:
#   a = [1,2,3]
#   A = [a,a,a]
# Since A now contains three times the same inner list a, changing a will affect
# all three lines. The line
#   A[0][2] = 5
# is equivalent to
#   a[2] = 5
# without changing the structure
#   A = [a,a,a]
# i.e. the change affects all three lines.

# ============================================================================ #
# Bonus Problem

# Internally, everything is references! In line 1 we create an empty list. In
# this, we add the list A itself *as a reference*, i.e. A contains itself, but
# not as a copy. Think of a piece of paper on which it is written how to find
# the piece of paper.
# 
# Memory model:
# -+-----------------------------+---------------------
#  | Element 0 of A:             |
#  | reference to memory cell X  |
# -+-----------------------------+---------------------
#   \                           /
#    \      memory cell X      /
# 
# Accordingly, reading A[0] yields A itself: the piece of paper is read, and you
# find some information; only that the found information is the same information
# you had before: A itself is a refrence to a memory cell as well.
# You can go to arbitrary depths: A == A[0] == A[0][0][0]...[0].
# 
# When overwriting (A[0][0] = 1) the list element with index 0 is changed, i.e.
# a new reference is put there:
# 
# -+-----------------------------+------+--------------
#  | Element 0 of A:             |   1  |
#  | reference to memory cell Y  |      |
# -+-----------------------------+------+--------------
#   \                           / \    /
#    \      memory cell X      /     Y
# 
# The original structure of the list A in memory is kept as is.
