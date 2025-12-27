class Solution:
    
    def solve(self,i,j,s1,s2,s3,memo):
        
        if i==len(s1) and j == len(s2) and (i+j) == len(s3):
            return True
        if ((i+j)>=len(s3)):
            return False
        if (i,j) in memo:
            return memo[(i,j)]
        result = False
        if i<len(s1) and s1[i] == s3[i+j]:
            result =  self.solve(i+1,j,s1,s2,s3,memo)
        if result == True:
            memo[(i,j)] = result
            return memo[(i,j)]
        if j < len(s2) and s2[j] == s3[i+j]:
            result = self.solve(i,j+1,s1,s2,s3,memo)
        memo[(i,j)] = result
        return memo[(i,j)]
    

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        m, n, l = len(s1), len(s2), len(s3)
        if m + n != l:
            return False
        
        result = self.solve(0,0,s1,s2,s3,memo)
        print(memo)
        return result