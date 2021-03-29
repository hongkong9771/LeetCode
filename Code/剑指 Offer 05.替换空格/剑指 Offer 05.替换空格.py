class Solution:
    def replaceSpace(self, s: str) -> str:
        res = []
        for i in s:
            if i == ' ':
                res.append("%20")
            else:
                res.append(i)
        return "".join(res)