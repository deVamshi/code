

import heapq
arr  = [3,2,3,1,2,4,5,5,6]
k = 2
pq = []

for num in arr:
    print('pushing ', num)
    heapq.heappush(pq, num)
    print("current pq is ",pq)
    if len(pq) > k:
        print("Length is greate than k, so poppping out")
        ele = heapq.heappop(pq)
        print("popped", ele)
        print("Now heap is ", pq)

print("out of for loop")
print(heapq.heappop(pq))




