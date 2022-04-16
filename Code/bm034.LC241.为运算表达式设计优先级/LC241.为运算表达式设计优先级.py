class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        """
        采用分治策略，以运算符（operator）为分界线，计算运算符左右两侧的结果，分别为x和y，然后计算x operator y即可。
        左右两侧的结果可以通过继续调用递归函数进行计算。
        有点类似于不同的二叉搜索树：
        将运算符看作根节点，叶子节点为数字。然后按后序遍历递归调用进行计算
        """
        if expression.isdigit():
            return [int(expression)]
        
        res = []
        for i, char in enumerate(expression):
            if char in ['+', '-', '*']:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for l in left:
                    for r in right:
                        if char == "+":
                            res.append(l + r)
                        elif char == "-":
                            res.append(l - r)
                        elif char == "*":
                            res.append(l * r)
        return res

