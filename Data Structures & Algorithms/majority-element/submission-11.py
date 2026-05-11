class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj=0
        dic={}
        for num in nums:
            dic[num]= dic.get(num,0)+1
        sortedDic=sorted(dic,key=dic.get, reverse=True)
        return sortedDic[0 ]
            