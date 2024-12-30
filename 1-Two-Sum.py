class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result={}
        for i,num in enumerate(nums):
            compliment=target-num
            if compliment in result:
                return [result[compliment],i]
            result[num]=i