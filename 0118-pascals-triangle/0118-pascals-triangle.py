class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = numRows
        result = [[0]]*(n)
        for i in range(n):
            result[i] = [1]*(i+1)
            for j in range(1,i):
                result[i][j] = result[i-1][j] + result[i-1][j-1]
        
        return result
