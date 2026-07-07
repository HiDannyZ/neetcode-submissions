import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}

        for n in nums:
            freqMap[n] = 1 + freqMap.get(n,0) #map the number of occurances

        maxHeap = [] #bc getting largest occurence
        for key,val in freqMap.items(): #.items() gets key value pair
            heapq.heappush(maxHeap,(-val,key)) #look into heapq ****(MAXHEAP VS MINHEAP) HOW DO THE HEAPS WORK

        res = []
        for n in range(k):
            res.append(heapq.heappop(maxHeap)[1]) #idk why 1 use one here, figure it out
        return res

        



        