# Last updated: 11/18/2025, 5:54:58 PM
class Solution:
    def twoSum(self, nums: List[int], target: int):
        prevMap = {}
        for i, n in enumerate(nums):
             diff = target - n
             if diff in prevMap:
                   return [prevMap[diff], i]
             prevMap[n] = i