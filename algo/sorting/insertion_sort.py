
def insertion_sort(arr):

    for i in range(len(arr)):
        key = arr[i]
        j = i - 1
        while (j >= 0 and arr[j] > key):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

print(insertion_sort([1,7,54,36,2,3,5]))

# in place comparison based sorting algorithm
# compares each element with all the previous elements and inserts into a desired loaction
#
# how it workds:
#
# 1. first step second element compares with the first element
# 2. In the second step the third elementcompares with the first two elements3.
# 3. In the last step the nth element compares with all the previous elements


# average = worst = O(n2)
# best cae = O(n)
