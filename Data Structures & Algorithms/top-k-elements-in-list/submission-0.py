import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # From what I remember, the heap is the most efficient algorithm in determining the 
        # the most frequent values
        freqMap = {}
        for num in nums:
            freqMap[num] = freqMap.get(num,0) + 1

        maxHeap = []
        for key,val in freqMap.items():
            heapq.heappush(maxHeap,(-val,key))
        res = []
        for _ in range(k):
            res.append(heapq.heappop(maxHeap)[1])
        return res

