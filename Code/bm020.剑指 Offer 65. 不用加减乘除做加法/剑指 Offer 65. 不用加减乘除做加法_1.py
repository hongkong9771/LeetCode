class Solution:
    def add(self, a: int, b: int) -> int:
        """
        由于python的数字存储特点，对于负数的存储形式不一样，
        需要进行特殊处理，建议使用Java完成这道题。
        """
        x = 0xffffffff
        a, b = a & x, b & x
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)