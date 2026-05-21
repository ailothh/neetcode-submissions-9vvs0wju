class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq=set(nums)
        maxcount=0
        for num in seq:
            count=0
            curnum= num
            if num-1 not in seq:
                while curnum in seq:
                    curnum+=1
                    count+=1
            maxcount=max(maxcount, count)
        return maxcount
                
        