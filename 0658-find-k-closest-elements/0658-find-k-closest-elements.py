class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        heapq.heapify(heap)
        for i in range(0,len(arr)):
            
            heapq.heappush(heap,[-abs(arr[i]-x),-arr[i]])
            while len(heap)>k:
                heapq.heappop(heap)
        res = [-heapq.heappop(heap)[1] for _ in range(k)]
        res.sort()
        
        
        return res
        