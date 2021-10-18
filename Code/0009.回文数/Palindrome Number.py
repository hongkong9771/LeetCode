class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        考虑将整数变为字符串，然后判断是否为回文数
        """
        s = str(x)

        if s[0] == '-':
            return False
        l = len(s)
        for i in range(l//2):
            if s[i] != s[l-i-1]:
                return False
        return True