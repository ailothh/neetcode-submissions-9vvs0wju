class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l,r =0, 0
        new=[]
        while l<len(word1) and r<len(word2):
            new.append(word1[l])
            new.append(word2[r])
            l+=1
            r+=1
        new.append(word1[l:])
        new.append(word2[r:])
        return "".join(new)
