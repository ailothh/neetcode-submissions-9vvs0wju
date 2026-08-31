class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicS={}
        dicT={}
        for letter in s:
            dicS[letter]= 1+dicS.get(letter,0)     
        for letter in t:
            dicT[letter]=1+dicT.get(letter ,0)
        return dicS==dicT