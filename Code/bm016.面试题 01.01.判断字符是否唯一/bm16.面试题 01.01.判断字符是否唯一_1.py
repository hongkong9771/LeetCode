class Solution:
    def isUnique(self, astr: str) -> bool:
        """
        用mark作为标记，记录每个字符出现的位置（用位运算做），假定字符均为a-z，则只需要一个26位的mark即可
        出现字符a，则无需移动（为001），出现字符b，则左移1位（为010），出现字符c，则左移2位（为100）。
        新出现的字符与mark相与，如果不为0，则说明以前该字符出现过；若为0，则说明以前该字符串未出现过。
        """
        mark = 0
        for char in astr:
            move_bit = ord(char) - ord('a')
            if (mark & 1 << move_bit) != 0:
                return False
            else:
                mark |= (1 << move_bit)
        return True