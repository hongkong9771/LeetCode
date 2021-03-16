class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        p = [[0]*n for zong in range(m)]        # 创建1个m*n的二维数组，用于储存走到每个位置的路径数
        for i in range(m):          # 初始化第1列为1
            p[i][0] = 1
        for j in range(n):          # 初始化第1行为1
            p[0][j] = 1
        for i in range(1,m):        
            for j in range(1,n):    
                p[i][j] = p[i-1][j]+p[i][j-1] # 由(i,j)位置的左边和上面的点的值确定该点处的值 
        return p[-1][-1]
