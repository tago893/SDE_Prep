class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest,s = 0,set(nums)

        for num in nums:
            current_length,j = 1,1
            while num-j in s:
                s.remove(num-j)
                current_length,j = current_length+1,j+1
            j= 1
            while num+j in s:
                s.remove(num+j)
                current_length,j = current_length+1,j+1
            longest = max(longest,current_length)
        
        return longest