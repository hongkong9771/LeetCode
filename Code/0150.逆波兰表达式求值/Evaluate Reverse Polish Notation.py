class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for l in tokens:
            if l == "+":
                stack.append(stack.pop()+stack.pop())       # 第一个pop为运算符前面的数，第二个pop为运算符后面的数
            elif l == "-":
                stack.append(-stack.pop()+stack.pop())
            elif l == "*":
                stack.append(stack.pop()*stack.pop())
            elif l == "/":
                stack.append(int(1/stack.pop()*stack.pop()))
            else:
                stack.append(int(l))
        return stack.pop()