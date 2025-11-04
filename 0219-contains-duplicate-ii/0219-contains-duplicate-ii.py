class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        duplicate_detect = {}
        for i,val in enumerate(nums):
            if len(duplicate_detect)>0 and val in duplicate_detect:
                prev_index = duplicate_detect[val]
                if (i - prev_index)<=k and nums[i] == nums[prev_index]:
                    return True
                
            duplicate_detect[val] = i
        return False