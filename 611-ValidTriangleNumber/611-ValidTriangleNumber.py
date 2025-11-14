# Last updated: 11/14/2025, 8:47:56 AM
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        count = 0

        # Fix the largest side nums[k]
        for k in range(n - 1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    # All elements between i and j form valid triangles with nums[j], nums[k]
                    count += (j - i)
                    j -= 1
                else:
                    i += 1

        return count
