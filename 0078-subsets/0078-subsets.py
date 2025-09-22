class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        def solve(i,combination):
            nonlocal result
            if i>=n:
                result.append(combination[:])
                return
            #take
            combination.append(nums[i])
            solve(i+1,combination)
            #not take
            combination.pop()
            solve(i+1,combination)
            

        solve(0,[])
        return result