class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #clarify rephrase
        #edge cases contraints 
        #tiem and space
        dic={}
        for num in nums:
            dic[num]= dic.get(num, 0)+1
        sortedDic= sorted(dic, key= dic.get, reverse=True)
        return sortedDic[:k]