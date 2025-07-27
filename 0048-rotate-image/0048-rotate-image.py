class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(0,len(matrix)):
            for j in range(i+1,len(matrix[0])):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
            print(matrix[i])

        for r in range(len(matrix)):
            l=0 
            h =len(matrix[r])-1
            while l<h:
                matrix[r][l],matrix[r][h] = matrix[r][h],matrix[r][l]
                l+=1
                h-=1
        
        