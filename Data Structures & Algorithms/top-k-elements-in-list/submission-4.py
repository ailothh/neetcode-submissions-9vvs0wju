class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        FreqCount= Counter(nums)
        sortedDic= sorted(FreqCount,key= FreqCount.get,reverse=True)
        return sortedDic[:k]