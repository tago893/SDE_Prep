class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        visited_matrix = [[False] * n for _ in range(n)]

        # Push all land cells
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                    visited_matrix[i][j] = True

        # If no land or all land -> impossible
        if not q or len(q) == n*n:
            return -1

        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        distance = -1

        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and not visited_matrix[nx][ny]:
                        visited_matrix[nx][ny] = True
                        q.append((nx, ny))
            distance += 1

        return distance
