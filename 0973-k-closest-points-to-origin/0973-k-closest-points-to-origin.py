class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest_points = []
        min_heap = []
        heapq.heapify(min_heap)
        for point in points:
            x = point[0]
            y = point[1]
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(min_heap,(dist,point))
        while len(closest_points)<k:
            _,point = heapq.heappop(min_heap)
            closest_points.append(point)
        return(closest_points)