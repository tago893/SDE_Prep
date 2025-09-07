class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        heap = []
        for passenger, from_t, to in trips:
            while heap and heap[0][0] <= from_t:
                _, num = heappop(heap)
                capacity += num
            heappush(heap, (to, passenger))
            capacity -= passenger
            if capacity < 0:
                return False
        return True