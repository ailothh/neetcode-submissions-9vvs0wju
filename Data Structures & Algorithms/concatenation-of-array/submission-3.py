class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(2):
            for letter in nums:
                ans.append(letter)
        return ans 