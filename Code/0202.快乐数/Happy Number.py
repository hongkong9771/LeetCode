class Solution:
    def isHappy(self, n: int) -> bool:
        """
        因为可能会出现无限循环，所以可以将中间计算的值保存在一个哈希表里（集合或者字典），
        当出现重复的值时，就直接返回false，因为此时已是在无限循环了，该数不可能为快乐数。
        """
        set1 = set()
        while n not in set1:
            set1.add(n)
            n = self.cal_square(n)
            if n == 1:
                return True
        return False



    def cal_square(self, num):
        result = 0
        num_str = str(num)
        l = len(num_str)
        for i in range(l):
            div = num // 10
            mod = num % 10
            num = div
            result += mod**2
        return result