class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        #采用切片的方式进行输出
        return s[n:]+s[:n]