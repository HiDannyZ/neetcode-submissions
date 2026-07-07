import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = []

        freqMap = {}
        maxHeap = []

        for num in nums:
            freqMap[num] = 1 + freqMap.get(num,0)

        for key,val in freqMap.items():
            heapq.heappush(maxHeap,(-val,key))
        
        for _ in range(k):
            res.append(heapq.heappop(maxHeap)[1])
        return res
            