class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        res = 0
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if int(matrix[i][j]) == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = int(min(
                            int(dp[i-1][j]),
                            int(dp[i][j-1]),
                            int(dp[i-1][j-1])
                        )) + 1
                    res = max(res,dp[i][j])
        return res*res