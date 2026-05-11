class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counted= Counter(nums)
        sort=sorted(counted,key=counted.get, reverse=True)
        return sort[0]
            