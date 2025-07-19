class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        max_seen_so_far = -1
        for i in range(n-2,-1,-1):
            temp = arr[i]
            arr[i] =  max(arr[i+1],max_seen_so_far)
            max_seen_so_far = temp
        arr[-1] = -1
        return arr

