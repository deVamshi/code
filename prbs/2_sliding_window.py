

# https://practice.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/
def maximumSumSubArray(arr, k, n):
    max_sum = float('-inf')
    curr_sum = sum(arr[0:k])
    
    for i in range(k, n):
        curr_sum = curr_sum + arr[i] - arr[i - k]
        max_sum = max(max_sum, curr_sum)

    return max_sum
            



# https://leetcode.com/problems/minimum-size-subarray-sum/submissions/
def minSubArrayLen(target, nums):
    min_len = float('inf')
    start = 0
    curr_sum = 0

    for end, val in enumerate(nums):
        curr_sum += val
        
        while curr_sum >= target:
            min_len = min(min_len, end - start + 1)
            curr_sum -= nums[start]
            start += 1
    
    return min_len if min_len != float('inf') else 0
