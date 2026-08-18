class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        final=[]
        for n in range(2):
            for num in nums: 
                final.append(num)
        return final 