class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        def solve(i,curr_list):
            if i >= n:
                result.append(curr_list[:])
                return 
            curr_list.append(nums[i])
            solve(i+1,curr_list)
            curr_list.pop()
            solve(i+1,curr_list)
        solve(0,[])
        return result