class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        memo = [[-1] * n for _ in range(m)]

        def dfs(i, j):

            if obstacleGrid[i][j] == 1:
                return 0

            if i == (m - 1) and j == (n - 1):
                return 1

            if i >= m or j >= n:
                return 0

            if memo[i][j] != -1:
                return memo[i][j]
            
            right = 0
            down = 0

            if i+1 < m:
                down = dfs(i+1, j)
            
            if j+1 < n:
                right = dfs(i, j+1) 
                

            memo[i][j] =  right + down 
            return memo[i][j]

        return dfs(0, 0)
        