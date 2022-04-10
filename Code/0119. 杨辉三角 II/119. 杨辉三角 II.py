class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        对于杨辉三角而言，每一行的第一个和最后一个均为1，中间的数字为上面数字两两相加之和,
        LC118题要求返回前numRows行，此处要求返回第rowIndex行，理论都是一样的。
        """
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        YhTri = [[1], [1,1]]
        for row in range(2, rowIndex+1):
            tmp = [1]
            for i in range(len(YhTri[(row-1)%2])-1):
                tmp.append(YhTri[(row-1)%2][i] + YhTri[(row-1)%2][i+1])
            tmp.append(1)
            YhTri[row%2] = tmp
        return YhTri[row%2]