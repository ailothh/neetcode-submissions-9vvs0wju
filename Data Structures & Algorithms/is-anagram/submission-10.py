class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        CountS={}
        CountT={}
        for letter in s:
            CountS[letter]= CountS.get(letter, 0)+1

        for letter in t:
            CountT[letter]= CountT.get(letter, 0)+1
        return CountT==CountS
