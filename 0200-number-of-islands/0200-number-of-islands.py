from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        cnt = 0
        vis = [[0 for _ in range(m)] for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and vis[i][j] == 0:
                    cnt += 1
                    q = deque()
                    q.append((i, j))
                    vis[i][j] = 1
                    
                    while q:
                        x, y = q.popleft()
                        
                        dx = [-1, 0, 1, 0]
                        dy = [0, 1, 0, -1]
                        
                        for k in range(4):
                            newx = x + dx[k]
                            newy = y + dy[k]
                            if 0 <= newx < n and 0 <= newy < m and \
                               grid[newx][newy] == '1' and vis[newx][newy] == 0:
                                q.append((newx, newy))
                                vis[newx][newy] = 1
        return cnt