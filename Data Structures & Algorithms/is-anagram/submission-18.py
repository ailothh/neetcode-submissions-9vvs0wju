
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #crete two hashmaps and compare them to eachother
        sMap={}
        tMap={}
        for num in s:
            sMap[num]= sMap.get(num,0)+1

        for num in t:
            tMap[num]=tMap.get(num, 0)+1
        return sMap==tMap
        