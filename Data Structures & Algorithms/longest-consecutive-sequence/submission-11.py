class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet=set(nums)
        res=0
        for num in numsSet:#loop thru 

        #check start seq
            if (num-1) not in numsSet:
                
                length=1
                while (num+length) in numsSet:
                    length+=1
                res=max(length ,res)
        #incerement count

        return res

