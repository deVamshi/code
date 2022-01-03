
arr = list(map(int, input("Enter list separated by space: ").split()))
k_value = int(input("Enter k value: "))
n = len(arr)

# Prints all the subs
def subs_w_sum_k(ind, array, k):
    if ind >= n:
        if sum(array) == k:
            print(array)
        return
    array.append(arr[ind])
    subs_w_sum_k(ind + 1, array, k) 
    array.pop()
    subs_w_sum_k(ind + 1, array, k) 

# returns count of all subs with sum k
def subs_w_sum_k_single(ind, array, k):
    if ind >= n:
        if sum(array) == k:
            print(array)
            return True
        return False
    array.append(arr[ind])
    if(subs_w_sum_k_single(ind + 1, array, k) == True): return True
    array.pop()
    if(subs_w_sum_k_single(ind + 1, array, k) == True): return True
    return False

def count_all_subs_w_sum_k(ind, array, k):
    if ind >= n:
        if sum(array) == k:
            return 1
        return 0
    array.append(arr[ind])
    l = count_all_subs_w_sum_k(ind + 1, array, k)
    array.pop()
    r = count_all_subs_w_sum_k(ind + 1, array, k)
    return l + r

print(count_all_subs_w_sum_k(0, [], k_value))
