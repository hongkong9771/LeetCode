class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:      # 判断两种特殊情况
            return n
        return self.fib(n-1) + self.fib(n-2)