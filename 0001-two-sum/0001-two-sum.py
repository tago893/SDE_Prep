class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        n = len(nums)
        t=[]
        hashmap = defaultdict(int)
        for i in range(0,n):
            diff = target - nums[i]
            if diff in hashmap:
                t= [hashmap[diff],i]
            else:
                hashmap[nums[i]] = i
        return t
