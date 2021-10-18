class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(')')
            elif s[i] == '[':
                stack.append(']')
            elif s[i] == '{':
                stack.append('}')
            # 遍历字符串的过程中，发现stack已经为空，说明右括号没有相应的左括号匹配
            # 遍历字符串的过程中，发现栈里没有要匹配上的字符
            elif len(stack) == 0 or s[i] != stack[-1]:
                return False
            else:
                stack.pop()         # 栈元素与s[i]相等，出栈
        return len(stack) == 0      # 若最后有多余的元素就返回False，说明左括号没有匹配到相应的右括号