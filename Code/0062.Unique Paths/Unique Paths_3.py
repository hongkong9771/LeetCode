class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        与第二个方法的区别在于将原来的2维数组变成了1维数组，减少空间内存的消耗，但是不是太好理解
        '''
        p = [1] * n
        for i in range(1, m):       
            for j in range(1, n):
                p[j] += p[j-1]
        return p[-1]
