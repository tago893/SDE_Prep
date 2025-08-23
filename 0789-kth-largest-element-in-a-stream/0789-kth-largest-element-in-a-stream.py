import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.stream = nums

    def add(self, val: int) -> int:
       heapq.heapify(self.stream)
       heapq.heappush(self.stream,val)
       while len(self.stream) > self.k:
           heapq.heappop(self.stream)
       return self.stream[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)