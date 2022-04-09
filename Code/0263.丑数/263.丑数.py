class Solution:
    def isUgly(self, n: int) -> bool:
        """
        根据丑数的定义可知：若n为丑数，则n首先为正整数，其次还需满足n=2^a*3^b*5^c，且a、b、c均为非负整数，当a=b=c=0时，n=1，为丑数。
        """
        if n <= 0:
            return False
        factors = [2, 3, 5]

        for factor in factors:
            while n % factor == 0:
                n = n / factor
        if n != 1:
            return False
        return True