# Thanks to Peter Hanukaev for this code

def binarySearch(target, xs):
    # assuming xs is sorted
    def go(xs, target, lo, hi):
        if lo == hi:
            return xs[lo] == target
        else:
            pivot = (lo + hi) // 2
            if xs[pivot] < target:
                return go(xs, target, pivot + 1, hi)
            else:
                return go(xs, target, lo, pivot)

    return go(xs, target, 0, len(xs) - 1) 
