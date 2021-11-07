# Thanks to Peter Hanukaev for this code

# Doing things like
#   myList[a:b]
# always creates a copy of the slice of the list. This takes time and slows down
# our algorithm.
#
# The below code avoids this by passing only indices on instead of the entire
# list
#
# For convenience, the algorithm comprises of an outer and an inner function:
# The end user does not need to know about the index business but only wants to
# provide the list and search term. Hence this is all what the outer function
# accepts as arguments
#
# The inner function really deals with the recursion, for which it needs
# additional, internal arguments.

def binarySearch(xs, target):
    def go(lo, hi):
        if lo == hi:
            return xs[lo] == target
        else:
            pivot = (lo + hi) // 2
            if xs[pivot] < target:
                return go(pivot + 1, hi)
            else:
                return go(lo, pivot)

    return go(0, len(xs) - 1)

data = [1, 5, 6, 7, 8, 42, 96, 666, 1337, 2112]
searchTerm = 42

print(binarySearch(data, searchTerm) , end="\n\n")      # test for middle element
print(binarySearch(data, 1)          , end="\n\n")      # test for first element
print(binarySearch(data, 2112)       , end="\n\n")      # test for last element
print(binarySearch(data, 2)          , end="\n\n")      # test for not in list

