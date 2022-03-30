class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        # 使用翻转法
        s = list(s)
        s[0:n] = reversed(s[0:n])
        s[n:] = reversed(s[n:])
        s.reverse()
        return "".join(s)