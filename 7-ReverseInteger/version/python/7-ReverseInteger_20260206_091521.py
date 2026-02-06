# Last updated: 2/6/2026, 9:15:21 AM
1class Solution:
2    def reverse(self, x: int) -> int:
3       sign = -1 if x < 0 else 1
4       rev = int(str(abs(x))[::-1]) * sign
5       return rev if -(2**31) <= rev <= ((2**31) - 1) else 0