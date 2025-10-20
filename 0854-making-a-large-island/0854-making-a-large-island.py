class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island_id = 2  # start from 2 to mark unique islands
        area_map = {}  # island_id -> area

        def dfs(r, c, id):
            if (r < 0 or r >= n or c < 0 or c >= n or grid[r][c] != 1):
                return 0
            grid[r][c] = id
            return (1 +
                    dfs(r + 1, c, id) +
                    dfs(r - 1, c, id) +
                    dfs(r, c + 1, id) +
                    dfs(r, c - 1, id))

        # 1️⃣ Label all islands and store their area
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    area = dfs(r, c, island_id)
                    area_map[island_id] = area
                    island_id += 1

        # Edge case: all land
        if not any(0 in row for row in grid):
            return n * n

        max_area = max(area_map.values(), default=0)

        # 2️⃣ Try flipping each 0 to 1 and merging adjacent islands
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()
                    area = 1  # flipped cell
                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            id = grid[nr][nc]
                            if id not in seen:
                                area += area_map[id]
                                seen.add(id)
                    max_area = max(max_area, area)

        return max_area
