class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l = 0
        r = len(arr) - 1
        missing_numbers = [0]*(len(arr))
        for i in range(len(arr)):
            missing_numbers[i] = arr[i] - (i+1)
        while l<=r:
            mid = l + (r-l)//2
            if missing_numbers[mid]<k:
                l = mid+1
            else:
                r = mid-1
        return l+k