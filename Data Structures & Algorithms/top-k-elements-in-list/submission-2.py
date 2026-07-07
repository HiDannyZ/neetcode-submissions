import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        theHeap = []
        res = []

        for n in nums:
            count[n] = 1 + count.get(n,0)
        
        for n, c in count.items():
            heapq.heappush(theHeap,(-c,n))

        for _ in range(k):
            res.append(heapq.heappop(theHeap)[1])
        return res

                