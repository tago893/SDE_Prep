class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        def backtrack(i,total):
            if i==n:
                return total
            
            with_ele = backtrack(i+1,total^nums[i])
            without_ele = backtrack(i+1,total)

            return with_ele + without_ele
            
        

        return backtrack(0,0)
        