class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        max_sum = float('-inf')
        max_array = []
        for i in range(0,len(nums)):
            sum += nums[i]
            if sum > max_sum:
                max_sum = sum
            max_array.append(nums[i])
            if sum<0:
                sum = 0
                max_array = []
        print(max_array)
        return max_sum


        