class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
    '''
    从网格的左上角走到网格的右下角，必定要经过m-1次向下移动和n-1次向右移动，总共需要移动m+n-2次，
    可以利用数学问题进行解决，即从m+n-2次移动中选m-1次向下移动，得到结果为：C_(m+n-2)^(m-1)，即
    (m+n-2)!/n!(m-2)!
    '''
        return comb(m+n-2, n-1)