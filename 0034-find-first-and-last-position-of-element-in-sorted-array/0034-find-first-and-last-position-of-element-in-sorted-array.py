class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        ans = [-1,-1]
        def find(l,r,target,firstOccurence):
            ans = -1
            while l<=r:
                mid = l + (r-l)//2
                if nums[mid]>target:
                    r = mid - 1
                elif nums[mid]<target:
                    l = mid+1
                else:
                    ans = mid
                    if firstOccurence:
                        r = mid-1
                    else:
                        l = mid+1
            return ans
        ans[0] = find(l,r,target,True)
        ans[1] = find(l,r,target,False)
        count = 0
        i = 0
        # while i<len(nums):
        #     ele = nums[i]
        #     count+=1
        #     last_index = find(i,len(nums)-1,ele,False)
        #     i = last_index+1
        # print(count)

        return ans