class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        i=0
        j=0
        row = len(matrix)
        cols = len(matrix[0])
        total =  row*cols
        top,bottom = 0,row-1
        left,right=0,cols-1

        while len(result)<total:
            # Traverse from left to right (top row)
            for col in range(left,right+1):
                if len(result)<total:
                    result.append(matrix[top][col])
            top+=1
            # Traverse top to bottom(right column)
            for row in range(top,bottom+1):
                if len(result)<total:
                    result.append(matrix[row][right])
            right-=1
            # Traverse from right to left(bottom row)
            for col in range(right,left-1,-1):
                if len(result)<total:
                    result.append(matrix[bottom][col])
            bottom-=1
            # Traverse bottom to top(left column)
            for row in range(bottom,top-1,-1):
                if len(result)<total:
                    result.append(matrix[row][left])
            left+=1


        return result
