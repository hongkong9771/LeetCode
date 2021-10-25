class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)     # 矩阵的行数
        n = len(matrix[0])  # 矩阵的列数
        l = list()
        # 当矩阵为空时，返回空列表
        if not matrix:
            return l        
        i, j = 0, 0
        top, bottom, left, right = 0, m-1, 0, n-1       # 定义上下左右四个边界，每遍历完一个边就收缩边界
        while True:
            for i in range(left, right+1):       # 顺时针向右走
                l.append(matrix[top][i])
            top += 1                             # top边界向下收缩
            if top > bottom:
                break
            for j in range(top, bottom+1):       # 顺时针向下走
                l.append(matrix[j][right])
            right -= 1                           # right边界向左收缩
            if right < left:
                break
            for k in range(right, left-1, -1):   # 顺时针向左走
                l.append(matrix[bottom][k])
            bottom -= 1                          # bottom边界向上收缩
            if bottom < top:
                break
            for o in range(bottom, top-1, -1):   # 顺时针向上走
                l.append(matrix[o][left])
            left += 1                            # left边界向右收缩
            if left > right:
                break
        return l