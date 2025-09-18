class Solution:
    def reverse(self,row: List[int]) -> List[int]:
        l = 0
        r = len(row) - 1
        while l<r:
            row[l],row[r] = row[r],row[l]
            l+=1
            r-=1

        return row
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i = 0
        j = 0
        n = len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        
        for i in range(n):
            matrix[i] = self.reverse(matrix[i])
        