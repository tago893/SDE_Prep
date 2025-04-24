class Solution:
    def reverse(self,nums:List[int],start:int) -> None:
        n = len(nums)
        end = len(nums)-1
        while start<end:
            nums[start],nums[end] = nums[end],nums[start]
            start+=1
            end-=1 
        
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        breakpoint_index = -1
        i = 0
        # Finding the longest prefix 
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                breakpoint_index = i
                break
        if breakpoint_index == -1:
            self.reverse(nums,0)
        else:    
            # Swap the next largest elemnet
            for i in range(n-1,-1,-1):
                if nums[i]>nums[breakpoint_index]:
                    nums[breakpoint_index],nums[i] = nums[i],nums[breakpoint_index]
                    break
            self.reverse(nums,breakpoint_index+1)
        
            

        