class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        combination = []
        candidates.sort()
        def backtrack(start,candidates,combination,target,total):
            if total == target:
                result.append(list(combination))
            elif total>target:
                return
            for i in range(start,len(candidates)):
                if(i>start and candidates[i]==candidates[i-1]):
                    continue
                combination.append(candidates[i])
                backtrack(i+1,candidates,combination,target,total+candidates[i])
                combination.pop()
        
        
        backtrack(0,candidates,combination,target,0)
        return result