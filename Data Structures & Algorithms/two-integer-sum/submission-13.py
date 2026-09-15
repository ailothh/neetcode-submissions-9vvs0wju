class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        #if key ===target return that key for that indice
        for i in range(len(nums)):
            num=nums[i]
            complement = target-num
            if complement in dic:
                return [dic[complement],i]
            dic[num]=i

