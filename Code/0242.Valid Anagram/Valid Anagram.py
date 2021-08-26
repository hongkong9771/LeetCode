class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        用一个字典，记录s字符串里每个字符出现的次数，然后当相同的字符出现在
        t字符串里时，依次减去该字符在字典中的次数，最后判断是字典里的数值否全为0

        """
        dict_st = {} # 记录每个字母出现的次数

        for i in range(len(s)):
            dict_st[s[i]] = dict_st.get(s[i],0) + 1
        
        for j in range(len(t)):
            dict_st[t[j]] = dict_st.get(t[j],0) - 1

        for value in dict_st.values():
            if value != 0:
                return False
        return True