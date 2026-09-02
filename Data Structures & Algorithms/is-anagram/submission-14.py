class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1={}
        dic2={}
        for letter in s:
            dic1[letter]=1+ dic1.get(letter,0)

        for letter in t:
            dic2[letter]=1+dic2.get(letter,0)
        return dic1==dic2