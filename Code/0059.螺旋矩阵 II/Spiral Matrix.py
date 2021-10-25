class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top, bottom, left, right = 0, n-1, 0, n-1
        # 创建一个n*n的矩阵
        matrix = [[0 for i in range(n)] for i in range(n)]
        num = 1
        while num <= n*n:
            for i in range(left, right+1):  # 顺时针向右遍历
                matrix[top][i] = num
                num += 1
            top += 1
            if top > bottom:
                break

            for j in range(top, bottom+1):  # 顺时针向下遍历
                matrix[j][right] = num
                num += 1
            right -= 1
            if right < left:
                break
            
            for k in range(right, left-1, -1):  # 顺时针向左遍历
                matrix[bottom][k] = num
                num += 1
            bottom -= 1
            if bottom < top:
                break

            for l in range(bottom, top-1, -1):  # 顺时针向上遍历
                matrix[l][left] = num
                num += 1
            left += 1
            if left > right:
                break
        return matrix
