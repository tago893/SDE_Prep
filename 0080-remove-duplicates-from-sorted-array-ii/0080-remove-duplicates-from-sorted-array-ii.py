class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j = 2,2
        n = len(nums)
        if n<=2:
            return n
        while j<n:
            if nums[j] != nums[i-2]:
                nums[i] = nums[j]
                i = i+1
            j = j+1
        return i
