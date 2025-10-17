class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [0,1], [-1,0], [0,-1], [1,1], [-1,-1], [1,-1], [-1,1]]
        ROWS, COLS = len(grid), len(grid[0])
        nodes = 0
        

        def bfs(r, c,nodes):
            q = deque()
            grid[r][c] = 1
            count = 1
            q.append((r, c,count))

            while q:
                row, col,count = q.popleft()
                if row ==0 and col ==0:
                    return count
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= ROWS or
                        nc >= COLS or grid[nr][nc] == 1
                    ):
                        continue
                    q.append((nr, nc,count+1))
                    grid[nr][nc] = 1
            return -1

        if grid[ROWS-1][COLS-1] == 0 :
            nodes+=bfs(ROWS-1, COLS-1, nodes)
                    
        if nodes == 0:
            return -1
        return nodes