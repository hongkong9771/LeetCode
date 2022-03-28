class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        思路：
        将p用字典存储起来，统计每个字母出现的次数。对于该字典的定义，其表示后面滑动窗口内的字符串
        需要对应元素的个数才满足异位词的要求然后对于字符串s而言，使用滑动窗口从左往右滑动，
        如果窗口内的字母出现在字典里，则字典里对应元素的次数减1，同时还维护一个计数器cnt=l_p，每当窗口
        出现一个对应元素，则cnt减1。在cnt动态更新的过程中，需要判断滑动窗口的字符串是否需要当前字符，
        才能对cnt进行更新操作，否则，不应进行更新
        当cnt=0时，表示窗口内的字符串与p满足字母异位词。
        """
        l_s = len(s)
        l_p = len(p)
        if l_s < l_p:
            return []
        dic = dict()
        cnt = l_p
        res = []
        # 统计字符串p里的每个字母出现的次数
        for i in p:
            dic[i] = dic.get(i, 0) + 1
        
        for j in range(l_p):
            if s[j] in dic:
                dic[s[j]] -= 1
                if dic[s[j]] >= 0:
                    cnt -= 1
        if cnt == 0:
            res.append(0)
        left, right = 1, l_p
        while right < l_s:
            if s[left-1] in dic:
                dic[s[left-1]] += 1
                if dic[s[left - 1]] > 0:  # 当滑动窗口内的字符串需要左侧去掉的s[left-1]字符时，即其个数大于0时，cnt才需要进行加1操作
                    cnt += 1
            if s[right] in dic:
                dic[s[right]] -=1
                if dic[s[right]] >= 0:  # 当滑动窗口内的字符串需要右侧新增的s[right]字符时，即其个数大于等于0时，cnt才需要进行减1操作
                    cnt -= 1
            if cnt == 0:
                res.append(left)
            left += 1
            right += 1
        return res
            
