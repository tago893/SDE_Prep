class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # even index have positive elements in the final array
        # odd index have negative elements in the final array

       pos = 0
       neg = 1
       i = 0
       res = [0]*(len(nums))
       while i<len(nums):
        if nums[i]>0:
            res[pos] = nums[i]
            pos+=2
        elif nums[i]<0:
            res[neg] = nums[i]
            neg+=2
        i+=1
       return res