class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        对于杨辉三角而言，每一行的第一个和最后一个均为1，中间的数字为上面数字两两相加之和
        """
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        YhTri = [[1],[1,1]]
        for row in range(2, numRows):
            tmp = [1]
            for i in range(len(YhTri[row-1])-1):
                tmp.append(YhTri[row-1][i] + YhTri[row-1][i+1])
            tmp.append(1)
            YhTri.append(tmp)
        return YhTri