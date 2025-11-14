# Last updated: 11/14/2025, 8:47:54 AM
class Solution:
    def minMoves(self, nums, limit):
        n = len(nums)
        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            low, high = min(a, b) + 1, max(a, b) + limit
            total = a + b

            # default add 2 moves for all sums
            diff[2] += 2
            diff[2 * limit + 1] -= 2

            # reduce to 1 move in [low, high]
            diff[low] -= 1
            diff[high + 1] += 1

            # reduce further to 0 moves at total
            diff[total] -= 1
            diff[total + 1] += 1

        ans, curr = float("inf"), 0
        for s in range(2, 2 * limit + 1):
            curr += diff[s]
            ans = min(ans, curr)

        return ans
