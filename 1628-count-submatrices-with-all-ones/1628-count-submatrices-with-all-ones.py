class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        def count(arr):
            consecutive_count = 0
            sub_count = 0
            for val in arr:
                if val==0:
                    consecutive_count=0
                else:
                    consecutive_count+=1
                sub_count+=consecutive_count
            return sub_count
                
        res =0 
        m = len(mat)
        n = len(mat[0])
        for start in range(m):
            row = [1]*(n)
            for end in range(start,m):
                for col in range(n):
                    row[col] = row[col]&mat[end][col]
                res+=count(row)
        return res