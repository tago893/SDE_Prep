class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum,rightsum = 0, sum(nums)
        for index,num in enumerate(nums):
            rightsum-=num
            if leftsum == rightsum:
                return index
            leftsum+=num
        return -1