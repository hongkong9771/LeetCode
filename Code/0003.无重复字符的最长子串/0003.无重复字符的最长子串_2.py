class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        if l <= 1:
            return l
        left, right = -1, 0
        res = 0
        """采用字典的形式存储不重复的字符串，总的时间复杂度为O(n)，空间复杂度为O(1)， 
        字符的ASCII码范围为0~127，哈希表 dic 最多使用O(128)=O(1)大小的额外空间。
        """
        d = dict()
        while right < l:
            if s[right] in d:
                left = max(d[s[right]], left)       # 当有重复的字符出现时，直接把左边界挪到出现重复的位置
            d[s[right]] = right
            res = max(res, right-left)
            right += 1
        return res