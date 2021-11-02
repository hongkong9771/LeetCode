class Solution:
    def compressString(self, S: str) -> str:
        if not S:
            return ""
        res = ""
        ch = S[0]
        cnt = 0
        for c in S:
            if c == ch:
                cnt += 1
            else:
                res += ch + str(cnt)
                cnt = 0
                ch = c
                cnt += 1
        res += ch + str(cnt)
        return res if len(res) < len(S) else S