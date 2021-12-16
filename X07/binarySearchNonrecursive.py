def binarySearch(data, searchTerm, start=0, end=-1) :
    if end < 0 : end = len(data) + end

    while start != end :
        mid = (start + end) // 2

        if   data[mid] == searchTerm : return True
        elif data[mid]  > searchTerm : end   = mid - 1
        else                         : start = mid + 1

    return False


data = [1, 5, 6, 7, 8, 42, 96, 666, 1337, 2112]

print(binarySearch(data, 42)  , end="\n\n")      # test for middle element
print(binarySearch(data, 1)   , end="\n\n")      # test for first element
print(binarySearch(data, 2112), end="\n\n")      # test for last element
print(binarySearch(data, 2)   , end="\n\n")      # test for not in list

