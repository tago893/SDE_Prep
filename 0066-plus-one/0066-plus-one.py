class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = 0
        for n in digits:
            result = 10*result+ n
        result = result+1
        answer = []
        while result > 0:
            answer.append(result%10)
            result//=10 # Remove the last digit
        answer = answer[::-1]
        return answer