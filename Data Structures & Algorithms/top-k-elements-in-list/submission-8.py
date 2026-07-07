class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Naive Approach: 2 Pass approach
        # Use a Hashmap to keep track of freq
        # Second pass to find k numbers
        
        # 1 Pass: Heap
        minHeap = []
        numCounter = {}

        for num in nums:
            numCounter[num] = 1 + numCounter.get(num,0)

        for key,val in numCounter.items():
            heapq.heappush(minHeap, (val,key))
        
        while len(minHeap) > k:
            heapq.heappop(minHeap)
        res = []
        for tup in minHeap:
            res.append(tup[1])
        return res
            
