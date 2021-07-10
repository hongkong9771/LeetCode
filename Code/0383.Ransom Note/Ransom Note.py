class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        使用字典存储ransom和magazine中每个字符出现的次数，
        然后判断ransom中每个字符出现的次数是否小于等于magazine相应字符出现的次数，
        如果小于等于，则为true，如果大于则为false
        """
        # isFlag = True
        dict_ransomNote = dict()
        dict_magazine = dict()
        for i in ransomNote:
            dict_ransomNote[i] = dict_ransomNote.get(i, 0) + 1
        
        for i in magazine:
            dict_magazine[i] = dict_magazine.get(i, 0) + 1
        
        for key, value in dict_ransomNote.items():
            if key not in dict_magazine or dict_magazine[key] < value:
                # isFlag = False
                return False
        return True