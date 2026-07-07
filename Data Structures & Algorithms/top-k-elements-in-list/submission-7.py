class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # (freq, val)
        maxHeap = []
        counterMap = {}
        res = []
        for num in nums:
            counterMap[num] = 1 + counterMap.get(num,0)
        
        for key,val in counterMap.items():
            heapq.heappush(maxHeap,(-val,key))
        
        for _ in range(k):
            res.append(heapq.heappop(maxHeap)[1])
        
        return res
            
        