class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        max_area = 0
        vis = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                area = 0
                if grid[i][j] == 1 and vis[i][j] == 0:
                    area += 1 
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
                               grid[newx][newy] == 1 and vis[newx][newy] == 0:
                               area+=1
                               q.append((newx, newy))
                               vis[newx][newy] = 1
                    max_area = max(area,max_area)
        return max_area