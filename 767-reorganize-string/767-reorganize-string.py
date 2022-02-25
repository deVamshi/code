class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        maxHeap = [[-count, char] for char, count in counter.items()]
        heapq.heapify(maxHeap)
        out = ""
        while len(maxHeap) > 1:
            currCount, currChar = heapq.heappop(maxHeap)
            nextCount, nextChar = heapq.heappop(maxHeap)
            out += currChar
            out += nextChar
            
            currCount += 1
            nextCount += 1
            if currCount != 0: heapq.heappush(maxHeap, [currCount, currChar])
            if nextCount != 0: heapq.heappush(maxHeap, [nextCount, nextChar])
                
        if len(maxHeap) != 0:
            [cnt, char] = heapq.heappop(maxHeap)
            if -cnt > 1: return ""
            else: out += char
        return out
            
            