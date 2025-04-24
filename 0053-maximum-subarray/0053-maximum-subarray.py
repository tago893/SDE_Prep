class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        max_sum = float('-inf')
        start =-1
        end = -1
        for i in range(0,len(nums)):
            if sum == 0:
                start = i
            sum += nums[i]
            if sum > max_sum:
                max_sum = sum
                start,end = start,i

            if sum<0:
                sum = 0
                max_array = []
        print(nums[start:end+1])
        return max_sum


        