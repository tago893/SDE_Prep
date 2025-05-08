class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1,-1]
        def helper(nums,target,firstOccurence):
            start = 0
            end = len(nums) - 1
            ans = -1
            while start<=end:
                mid = start + (end-start)//2
                if nums[mid] > target:
                    end = mid - 1
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    ans = mid
                    if firstOccurence:
                        end = mid - 1
                    else:
                        start = mid + 1
            
            return ans
        ans[0] = helper(nums,target,firstOccurence=True)
        if ans[0]!=-1:
            ans[1] = helper(nums,target,firstOccurence=False)
        return ans

