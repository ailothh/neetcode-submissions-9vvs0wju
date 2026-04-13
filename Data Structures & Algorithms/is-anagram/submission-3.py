class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        sDic = {}
        tDic = {}
        for i in range(len(s)):
            sDic[s[i]] = 1+sDic.get(s[i], 0)
            tDic[t[i]]= 1 + tDic.get(t[i],0)
        return sDic==tDic
