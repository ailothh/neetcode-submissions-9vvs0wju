class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=nums[0]
        for i in range(len(nums)):
            count =0
            for j in range(i, len(nums)):
                count+=nums[j]
                res=max(res, count)
        return res