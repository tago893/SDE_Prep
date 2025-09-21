class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n):
            if i>0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n):
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                l = j+1
                r = n-1
                while l<r:
                    if nums[i]+nums[j]+nums[l]+nums[r] == target:
                        result.append([nums[i],nums[j],nums[l],nums[r]]) 
                        l+=1
                        r-=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                        while l<r and nums[r]==nums[r+1]:
                            r-=1
                        
                            
                    elif nums[i]+nums[j]+nums[l]+nums[r] > target:
                        r-=1
                    else:
                        l+=1
                

        return result