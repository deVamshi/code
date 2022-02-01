#User function Template for python3
# https://practice.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1

# first count the frequnce of the required num
# only then add it to the hashmap

# using brute force you can solve it by using two for loops

class Solution:
    def getPairsCount(self, arr, n, k):
        out = 0
        hashMap = {}
        for ele in arr:
            out += hashMap.get(k - ele, 0)
            hashMap[ele] = hashMap.get(ele, 0) + 1
                        
        return out
