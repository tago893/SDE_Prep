class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1,n+1)]
        result = []
        nums.sort()
        def solve(i,combination):
            if len(combination) == k:
                result.append(combination[:])
            for s in range(i,n):
                if s>i and nums[s] == nums[s-1]:
                    continue
                combination.append(nums[s])
                solve(s+1,combination)
                combination.pop()
            

        solve(0,[])
        return result