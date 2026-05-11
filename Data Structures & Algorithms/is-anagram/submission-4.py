class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sortedstr1, sortedstr2= sorted(s), sorted (t)
        if sortedstr1==sortedstr2:
            return True
        return False