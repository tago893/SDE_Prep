class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        t = {}
        for i in range(len(nums)):
            if nums[i] in t:
                t[nums[i]] += 1
            else:
                t[nums[i]] = 1
        
        pq = []
        for num in t.keys():
            heapq.heappush(pq,(t[num],num))
            if len(pq)>k:
                heapq.heappop(pq)
        res = []
        for i in range(k):
            res.append(heapq.heappop(pq)[1]) 
        return res       