# https://leetcode.com/problems/kth-largest-element-in-an-array/



# Sol using a heap
import heapq
arr  = [3,2,3,1,2,4,5,5,6]
k = 2
pq = []

for num in arr:
    # print('pushing ', num)
    heapq.heappush(pq, num)
    # print("current pq is ",pq)
    if len(pq) > k:
        # print("Length is greate than k, so poppping out")
        ele = heapq.heappop(pq)
        # print("popped", ele)
        # print("Now heap is ", pq)

# print("out of for loop")
# print(heapq.heappop(pq))

# Sol using sorting
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, reverse=True)
        return nums[k - 1]




