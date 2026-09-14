class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic={}
        for num in nums:
            dic[num]=dic.get(num, 0)+1
        return max(dic, key=dic.get)