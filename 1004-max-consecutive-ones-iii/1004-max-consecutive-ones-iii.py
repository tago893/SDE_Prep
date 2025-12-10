class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        n = len(nums)
        count = 0
        zeroCount = 0
        while j<n:
            if nums[j] == 0:
                zeroCount+=1
            while zeroCount>k:
                if nums[i] == 0:
                   zeroCount-=1
                i+=1
            count = max(count,j-i+1)
            j+=1
        return count

