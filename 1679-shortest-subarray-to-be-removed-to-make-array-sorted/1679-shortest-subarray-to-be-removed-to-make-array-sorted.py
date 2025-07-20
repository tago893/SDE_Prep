class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        left = 0
        right = 0
        n = len(arr)
        while left+1<n and arr[left] <= arr[left+1]:
            left+=1
        if left == n-1:
            return 0
        right = n-1
        while right-1>0 and arr[right] >= arr[right-1]:
            right-=1
        result = min(n-left-1,right)
        i=0
        j=right
        while i<=left and j<n:
            if arr[i]<=arr[j]:
                result = min(result,j-i-1)
                i+=1
            else:
                j+=1
        return result