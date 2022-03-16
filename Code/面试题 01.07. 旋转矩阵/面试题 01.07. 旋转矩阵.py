class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        此题是顺时针旋转90°，所以可以先以主对角线为对称轴，翻转，然后再以中心竖线为对称轴翻转
        若是逆时针旋转90°，则可以先以反主对角线为对称轴，翻转，然后再以中心竖线为对称轴翻转
        """
        n = len(matrix)
        for i in range(n):
            # 顺时针旋转的情况
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            # 逆时针旋转的情况
            # for j in range(0, n-1-i):
            #     matrix[i][j], matrix[n-1-j][n-1-i] = matrix[n-1-j][n-1-i], matrix[i][j]
            
            for j in range(n//2):
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]