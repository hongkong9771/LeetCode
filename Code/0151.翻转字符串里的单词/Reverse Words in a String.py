class Solution:
    def reverseWords(self, s: str) -> str:
        # 去掉空格
        s = s.split()
        # 反转
        s = reversed(s)
        # 加入空格，返回字符串
        return " ".join(s)