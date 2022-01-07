# https://leetcode.com/problems/reorganize-string/

# First, take the most frequent char and add it to out and then store this current one in a
# prev var and take the next most frequent char and it to output and push the prev to heap and
# store the current one in prev and continue
# we don't have max heap in python so we use minHeap
# which is built in python
# Counter is used for counting the frequency of each char

class Solution:
    def reorganizeString(self, s: str) -> str:
        
        counter = Counter(s)
        
        maxHeap = [[-cnt, char] for char, cnt in counter.items()]
        
        heapq.heapify(maxHeap)
        
        prev = None
        out = ''
        
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            
            cnt, char = heapq.heappop(maxHeap)
            out += char
            cnt += 1
            
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
                
            if cnt != 0:
                prev = [cnt, char]
                
        return out
            
        