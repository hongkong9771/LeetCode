class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        """
        方法三：排序
        """
        l1 = list(s1)
        l2 = list(s2)

        l1.sort()
        l2.sort()

        return l1 == l2