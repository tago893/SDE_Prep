class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a, b):
            a, b = str(a), str(b)
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0
        
        nums.sort(key=cmp_to_key(compare))
        if nums[0] == 0:
            return "0"
        
        ans = ""
        for num in nums:
            ans+=str(num)
        return ans