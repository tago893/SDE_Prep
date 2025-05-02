from collections import deque
class Solution:
    def bfs(self,grid,vis,q,cnt):
        drow = [-1,0,1,0]
        dcol = [0,1,0,-1]
        m = len(grid)
        n = len(grid[0])
        made,sec =0,0
        while q:
            r,c,sec = q.popleft()
            vis[r][c]=2
            for i in range(4):
                new_r = r + drow[i]
                new_c = c + dcol[i]
                if new_r>=0 and new_c>=0 and new_r<m and new_c<n and vis[new_r][new_c] != 2 and grid[new_r][new_c]==1:
                    q.append((new_r,new_c,sec+1))
                    made+=1
                    vis[new_r][new_c]=2
        return sec if made==cnt else -1
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        x = len(grid)
        y = len(grid[0])
        vis = [[0 for _ in range(y)]for _ in range(x)]
        cntFresh = 0
        q = deque()
        for i in range(x):
            for j in range(y):
                if grid[i][j] == 2:
                    q.append((i,j,0))
                if grid[i][j]==1:
                    cntFresh+=1
        print(vis)
        return self.bfs(grid,vis,q,cntFresh)
        



                        
