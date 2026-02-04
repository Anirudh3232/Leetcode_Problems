# Last updated: 2/4/2026, 7:14:48 AM
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        l = 1
4
5        for r in range(l, len(nums)):
6            if nums[r] != nums[r - 1]:
7                nums[l] = nums[r]
8                l += 1
9        return l