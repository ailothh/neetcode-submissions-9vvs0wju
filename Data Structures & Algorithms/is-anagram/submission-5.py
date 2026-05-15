class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1={}
        dic2={}
        for num in s:
            dic1[num]= dic1.get(num,0)+1 
        for num in t:
            dic2[num]= dic2.get(num,0)+1 
        return dic1==dic2
