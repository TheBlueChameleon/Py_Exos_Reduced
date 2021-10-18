# ============================================================================ #
# Problem 1

import math

myList = ["Dusky", "Joe", "Hartington"]

print("### ELEMENTS IN MODULE MATH:")
print(dir(math))
print()

print("### ELEMENTS IN CLASS LIST:")
print(dir(myList))

# ============================================================================ #
# Problem 6

A = [ [1,2,3] ] * 3
print(A)
A[0][2] = 5
print(A)
