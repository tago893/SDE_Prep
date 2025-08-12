class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # even index have positive elements in the final array
        # odd index have negative elements in the final array

        plus_int = []
        minus_int = []

        for num in nums:
            if num>0:
                plus_int.append(num)
            else:
                minus_int.append(num)
        i = 0
        j = 0
        res = []
        k = 0
        while i<len(plus_int) or j<len(minus_int):
            if k%2 == 0:
                res.append(plus_int[i])
                i+=1
            elif k%2!=0:
                res.append(minus_int[j])
                j+=1
            k+=1
        return res
