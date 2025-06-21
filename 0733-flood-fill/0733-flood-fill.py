class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(row,col,color,initColor,ans,dr,dc):
            ans[row][col] = color
            print([row,col])
            for i in range(4):
                nr = row+dr[i]
                nc = col+dc[i]
                print([nr,nc])
                if nr>=0 and nc>=0 and nr<len(image) and nc<len(image[0]) and image[nr][nc]==initColor and ans[nr][nc]!=color:
                    print("yya")
                    dfs(nr,nc,color,initColor,ans,dr,dc)  
            return
        

        ans = image.copy()
        initColor = image[sr][sc]
        dr = [-1,0,+1,0]
        dc = [0,-1,0,+1]
        dfs(sr,sc,color,initColor,ans,dr,dc)
        return ans