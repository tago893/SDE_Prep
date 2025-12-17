class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total%k != 0:
            return False
        
        target = total//k
        nums.sort(reverse=True)
        used = [False]*(len(nums))

        def backtrack(i,current_sum,groups_formed):
            if groups_formed == k:
                return True
            
            if current_sum == target:
                return backtrack(0,0,groups_formed+1)
            for j in range(i,len(nums)):
                if used[j] or current_sum+nums[j]>target:
                    continue
                if j>0 and not used[j-1] and nums[j]==nums[j-1]:
                    continue
                used[j] = True
                if backtrack(j+1,current_sum+nums[j],groups_formed):
                    return True
                used[j] = False

                if current_sum == 0:
                    return False
            return False
        
        return backtrack(0,0,0)