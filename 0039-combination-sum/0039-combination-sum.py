class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        # recursive function
        def solve(start,total,current_list):
            if total>target or start == n:
                return
            if total == target:
                res.append(current_list[:])
            for i in range(start,n):
                current_list.append(candidates[i])
                solve(i,total+candidates[i],current_list)
                current_list.pop()
                
        solve(0,0,[])
        return res