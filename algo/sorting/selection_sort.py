
def selection_sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

print(selection_sort([2,1,0,5,6,-1,-4]))

# Time complexity O(n2)
# best case = avg case = worst case = O(n2)

# selection sort is more 60% efficient than bubble bubble_sort
# easy to implement
# used for small data sets
# runninng time is veru poor(O(n2))
# insertion sort is better than selection sort


#  what is an inplace sorting alforthm
#  it needs O(1) or O(logn) memory to create auxillary locations
