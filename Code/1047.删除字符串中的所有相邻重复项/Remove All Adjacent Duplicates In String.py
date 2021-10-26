class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for s in S:
            if len(stack) != 0 and stack[-1] == s:      # 当元素重复时，出栈
                stack.pop()
            else:
                stack.append(s)                         # 当元素不重复时，入栈
        return "".join(stack)