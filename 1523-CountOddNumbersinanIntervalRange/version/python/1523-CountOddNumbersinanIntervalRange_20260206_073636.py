# Last updated: 2/6/2026, 7:36:36 AM
1class Solution:
2    def countOdds(self, low: int, high: int) -> int:
3        return (high + 1) // 2 - low // 2
4     