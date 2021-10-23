class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        从右上角向左下角遍历
        """
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False