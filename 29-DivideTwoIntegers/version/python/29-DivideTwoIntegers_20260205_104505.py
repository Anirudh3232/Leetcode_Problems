# Last updated: 2/5/2026, 10:45:05 AM
1class Solution:
2    def searchInsert(self, nums: List[int], target: int) -> int:
3        for i in range(len(nums)):
4            if nums[i] >= target:
5             return i
6        return len(nums)
7