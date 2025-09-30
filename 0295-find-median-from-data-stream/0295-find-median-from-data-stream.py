class MedianFinder:

    def __init__(self):
        # Max-heap for smaller half (simulated with negative values)
        self.maxHeap = []

        # Min-heap for larger half
        self.minHeap = []

    # Function to add a number to the data stream
    def addNum(self, num):
        # Step 1: Push to maxHeap (negate to simulate max-heap)
        heapq.heappush(self.maxHeap, -num)

        # Step 2: Move the largest from maxHeap to minHeap
        heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

        # Step 3: Balance the heaps if needed
        if len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    # Function to find the median
    def findMedian(self):
        if len(self.minHeap) == len(self.maxHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2.0
        return -self.maxHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()