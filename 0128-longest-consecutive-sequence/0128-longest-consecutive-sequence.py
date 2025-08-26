class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_longest = 0
        hash_set = set(nums)

        for num in hash_set:
            
            if num-1 not in hash_set:#we are finding the start of the sequence
                longest = 1
                temp = num
                while temp+1 in hash_set:
                    longest+=1
                    temp+=1
                max_longest = max(longest,max_longest)

        return max_longest 