import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num] = 1
        
        elements = [(-count,key) for key,count in freq.items()]
        heapq.heapify(elements)
        res = []
        while k>0:
            _,ele = heapq.heappop(elements)
            res.append(ele)
            k-=1
        return res
        




