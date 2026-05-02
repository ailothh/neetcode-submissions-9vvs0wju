class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for num in nums:
            dic[num]=dic.get(num,0)+ 1
        sortedarr= sorted(dic, key = dic.get, reverse=True)
        return sortedarr[:k]