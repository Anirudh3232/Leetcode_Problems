# Last updated: 2/8/2026, 11:44:15 AM
1class Solution:
2    def countOdds(self, low: int, high: int) -> int:
3        
4        return (high + 1) // 2 - (low // 2)