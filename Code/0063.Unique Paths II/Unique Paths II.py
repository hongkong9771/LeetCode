class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        p = [[0]*n for k in range(m)]
        for i in range(0, m):
            if obstacleGrid[i][0] == 1:         # 当碰到障碍物的时候，二维数组p后面的值保持0不变，因为已经无法到达后面了
                break
            p[i][0] = 1
        for j in range(0, n):
            if obstacleGrid[0][j] == 1:         # 同上一步
                break
            p[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:     # 当碰到障碍物时，到达此点的路径数为0，故该点处的p值依旧为0
                    continue
                p[i][j] = p[i-1][j] + p[i][j-1]
        return p[-1][-1]