class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        对每个字符串进行排序，排序后相同的字符串即为字母异位词，将排序后的字符串作为key，
        原字符串以列表的形式存储为key。
        """
        dic = dict()
        res = []
        for s in strs:
            tmp = "".join(sorted(s))
            if tmp not in dic:
                dic[tmp] = [s]
            else:
                dic[tmp].append(s)
        for values in dic.values():
            res.append(values)
        return res