class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = [0]*(n)
        prefix = -1
        result[n-1] = prefix
        for i in range(n-2,-1,-1):
            result[i] =  max(result[i+1],arr[i+1])
        
        return result

