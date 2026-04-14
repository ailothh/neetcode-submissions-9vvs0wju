class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Now find which key has the highest value
        for num in count: # loops through keys
            if count[num] > len(nums) // 2:
                return num # returns the key
