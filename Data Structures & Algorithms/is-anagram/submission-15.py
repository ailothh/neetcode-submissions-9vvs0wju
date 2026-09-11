class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicS={}
        dicT={}
        for letter in s:
            dicS[letter]=dicS.get(letter, 0)+1
        for letter in t:
            dicT[letter]=dicT.get(letter, 0)+1
        return dicS==dicT
        
