class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        if l <= 1:
            return l
        left, right = 0, 0
        res = 0
        while right < l:
            if s[right] in s[left:right]:
                left += 1
            else:
                right += 1
            res = max(res, right-left)
        return res