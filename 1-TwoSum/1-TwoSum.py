# Last updated: 11/21/2025, 7:59:37 AM
class Solution:
    def twoSum(self, nums: List[int], target: int):
        prevMap = {}
        for i, n in enumerate(nums):
             diff = target - n
             if diff in prevMap:
                   return [prevMap[diff], i]
             prevMap[n] = i