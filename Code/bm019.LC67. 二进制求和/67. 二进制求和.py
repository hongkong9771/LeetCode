class Solution:
    def addBinary(self, a: str, b: str) -> str:
        la = len(a)
        lb = len(b)
        if la > lb:
            b = "0" * (la - lb) + b
        else:
            a = "0" * (lb - la) + a
        
        flag = True            # 用于判断是否停止迭代
        lsum, ljin = "", ""
        while flag:
            for i in range(len(a)):
                lsum = lsum + str(int(a[i]) ^ int(b[i]))        # 求和
                ljin = ljin + str(int(a[i]) & int(b[i]))        # 进位
            a = "0" + lsum
            b = ljin + "0"
            lsum, ljin = "", ""
            if "1" not in b:
                flag = False
        if a.lstrip("0") == "":
            return "0"
        else:
            return a.lstrip("0")