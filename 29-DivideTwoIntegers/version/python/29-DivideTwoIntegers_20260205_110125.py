# Last updated: 2/5/2026, 11:01:25 AM
1class Solution:
2    def lengthOfLastWord(self, s: str) -> int:
3       return len(s.strip().split(' ') [-1])
4        