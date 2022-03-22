class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        def self_divide(n):
            a = n
            while a != 0:
                tmp = a % 10
                if tmp != 0:
                    if n % tmp != 0:
                        return False
                else:
                    return False
                a = a // 10
            return True
        
        res = []
        for i in range(left, right+1):
            if self_divide(i):
                res.append(i)
        return res