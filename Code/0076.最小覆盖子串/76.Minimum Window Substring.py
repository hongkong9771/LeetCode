class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for tt in t:
            need[tt] = need.get(tt, 0) + 1  # s中需要满足最小子串的字符以及对应数量
        cnt = len(t)  # 总的应该满足的数量

        left, right = 0, 0
        res = s + "a"
        while right < len(s):
            # 找到右边界
            while right < len(s) and cnt > 0:
                if need.get(s[right], 0) > 0:
                    cnt -= 1
                need[s[right]] = need.get(s[right], 0) - 1
                right += 1
            if cnt == 0:
                num = need.get(s[left])  # 当前字符在need中所需要的个数
                while num < 0:
                    need[s[left]] = num + 1
                    left += 1
                    num = need.get(s[left])
                # 确定左边界，则满足条件的子串被确定了
                if len(res) > len(s[left:right]):
                    res = s[left:right]
                cnt += 1
                need[s[left]] = need.get(s[left]) + 1
                left += 1
        if res == s + "a":      # 表示从未更新过
            return ""
        else:
            return res