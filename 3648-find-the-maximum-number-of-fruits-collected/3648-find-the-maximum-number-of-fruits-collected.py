class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        def child1_fruits(fruits) -> int:
            count = 0
            for i in range(0,n):
                count += fruits[i][i]
            return count
        
        def child2_fruits(i,j,fruits,memo):
            if i>=n or j<0 or j>=n:
                return 0
            if i==n-1 and j == n-1:
                return 0
            if i == j or i>j:
                return 0 
            if memo[i][j] != -1:
                return memo[i][j]       
            bottomleft = fruits[i][j] + child2_fruits(i+1,j-1,fruits,memo)
            bottom = fruits[i][j] + child2_fruits(i+1,j,fruits,memo)
            bottomright = fruits[i][j] + child2_fruits(i+1,j+1,fruits,memo)
            
            memo[i][j] = max(bottomleft,bottomright,bottom)
            return memo[i][j]
        
        def child3_fruits(i,j,fruits,memo):
            if i>=n or j<0 or j>=n:
                return 0
            if i==n-1 and j == n-1:
                return 0
            if i == j or i<j:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            upRight = fruits[i][j] + child3_fruits(i-1,j+1,fruits,memo)
            right = fruits[i][j] + child3_fruits(i,j+1,fruits,memo)
            bottomright = fruits[i][j] + child3_fruits(i+1,j+1,fruits,memo)
            memo[i][j] = max(upRight,right,bottomright)
            return memo[i][j]
        n = len(fruits)
        memo = [[-1 for _ in range(n)]for _ in range(n)]
        c1 = child1_fruits(fruits)
        c2 = child2_fruits(0,n-1,fruits,memo)
        c3 = child3_fruits(n-1,0,fruits,memo)

        return c1+c2+c3