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

            # Can remove the smallest frequency when the heap exceeds size k
            # maxHeap requires I store every element.
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        res = []
        for _ in range(k):
            res.append(minHeap.pop()[1])
        return res
            
