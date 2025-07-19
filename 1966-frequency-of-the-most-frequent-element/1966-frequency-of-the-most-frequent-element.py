class Solution:
    def binary_search(self,target_idx,nums,prefix,k):
        l = 0
        r = target_idx
        
        best_index = target_idx
        while l<=r:
            mid = l + (r-l)//2
            count = target_idx - mid + 1
            count_sum = count*nums[target_idx]
            original_sum = prefix[target_idx] - prefix[mid] + nums[mid]
            diff = count_sum - original_sum
            if diff>k:
                l = mid+1
            else:
                best_index = mid
                r = mid-1
        
        return target_idx - best_index + 1
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        frequency = 0
        result = 0
        prefix_arr = [0]*(n)
        prefix_arr[0] = nums[0]
        for i in range(1,n):
            prefix_arr[i] = prefix_arr[i-1] + nums[i]
        for i in range(0,n):
            frequency = self.binary_search(i,nums,prefix_arr,k)
            result = max(frequency,result)
        return result


