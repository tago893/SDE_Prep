import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)

        for num in nums:
            heapq.heappush(heap,-num)
        ele = heap[0]
        while k>0:
            k-=1
            ele = heapq.heappop(heap)
        return (-ele)
        