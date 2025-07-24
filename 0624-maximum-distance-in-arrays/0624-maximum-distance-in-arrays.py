class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        final_max = arrays[0][-1]
        final_min = arrays[0][0]
        max_distance = 0
        for i in range(1,len(arrays)):
            arr = arrays[i]
            max_distance = max(max_distance,abs(final_min - arr[-1]),abs(final_max - arr[0]))
            final_max = max(final_max,arr[-1])
            final_min = min(final_min,arr[0])
            
        return max_distance