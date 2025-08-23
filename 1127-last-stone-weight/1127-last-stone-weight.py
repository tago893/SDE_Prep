import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while True:
            if len(stones) == 1 or len(stones) == 0:
                break
            stones = [-x for x in stones]
            heapq.heapify(stones)
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)

            if y!=x:
                heapq.heappush(stones,y-x)
            stones = [-x for x in stones]
            
        return stones[0] if len(stones)==1 else 0