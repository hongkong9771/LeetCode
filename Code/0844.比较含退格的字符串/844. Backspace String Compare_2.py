class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        解题思路：
        每一个"#"均只删除其前面的字符，因此，可以考虑从后往前进行遍历。并定义skipS和skipT对"#"进行计数
        此时，一共有以下几种情况：
        1.当前字符为"#"时，skipS加1；
        2.当前字符不为"#"时，若skipS>0，则删除当前字符，即skipS减1；
        3.当前字符不为"#"时，若skipS=0，则当前字符无需删除，skipS值不变，并将当前字符取出来用于后面的比较。
        遍历截止的条件为：
        两个字符串均完成遍历，或者中间有字符不相等
        """
        i, j = len(s)-1, len(t)-1
        skipS, skipT = 0, 0

        while i >= 0 or j >= 0:
            # 先进入字符串s的循环
            while i >= 0:
                if s[i] == "#":         # 情况1
                    skipS += 1
                    i -= 1
                elif s[i] != "#":       # 情况2
                    if skipS > 0:
                        skipS -= 1
                        i -= 1
                    else:               # 情况3
                        break  
            # 再进入字符串t的循环
            while j >= 0:
                if t[j] == "#":         # 情况1
                    skipT += 1
                    j -= 1
                elif t[j] != "#":       # 情况2
                    if skipT > 0:
                        skipT -= 1
                        j -= 1
                    else:               # 情况3
                        break
            # 对情况3下的字符进行比较
            if i >= 0 and j >= 0:
                if s[i] == t[j]:
                    i -= 1
                    j -= 1
                else:
                    return False        # 如果值不相同，直接返回False
            elif i >= 0 or j >= 0:      # 一个已经没有字符了，另外一个还有字符，返回False
                return False
        return True                     # 两个字符串均能顺利全部遍历完，则说明两个字符串相等，返回True