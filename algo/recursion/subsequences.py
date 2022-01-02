arr = list(map(int, input().split()))
n = len(arr)

def printSubs(ind, array):
    
    if ind >= n:
        print(array)
        return
    array.append(arr[ind])
    printSubs(ind + 1, array)
    array.pop()
    printSubs(ind + 1, array)

printSubs(0, [])