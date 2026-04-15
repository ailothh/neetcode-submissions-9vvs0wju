class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=1
        res =nums[0]
        for num in range(1,len(nums)):
            if count==0:
                res = nums[num]
            if nums[num] != res:
                count-=1
            if nums[num]==res:
                count+=1
        return res
                
