# Last updated: 5/20/2026, 3:08:36 AM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        num_map = {}
4        for i, num in enumerate(nums):
5            complement = target - num
6            if complement in num_map:
7                return [num_map[complement], i]
8            num_map[num] = i
9