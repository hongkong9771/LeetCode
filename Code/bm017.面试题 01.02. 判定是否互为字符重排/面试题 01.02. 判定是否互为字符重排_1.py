class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        """
        方法一：统计字符
        """
        dict_char1 = dict()
        dict_char2 = dict()
        for char1 in s1:
            dict_char1[char1] = dict_char1.get(char1, 0) + 1
        for char2 in s2:
            dict_char2[char2] = dict_char2.get(char2, 0) + 1
        
        if len(dict_char1) != len(dict_char2):
            return False

        for char1 in dict_char1.keys():
            if char1 not in dict_char2 or dict_char2[char1] != dict_char1[char1]:
                return False
        return True