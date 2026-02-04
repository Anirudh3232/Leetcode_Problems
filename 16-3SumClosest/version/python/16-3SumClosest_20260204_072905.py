# Last updated: 2/4/2026, 7:29:05 AM
1class Solution:
2    def removeElement(self, nums: List[int], val: int) -> int:
3        index = 0
4
5        for i in range(len(nums)):
6            if nums[i] != val:
7                nums[index] = nums[i]
8                index += 1
9        return index