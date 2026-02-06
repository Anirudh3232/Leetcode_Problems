# Last updated: 2/6/2026, 6:55:59 AM
1class Solution:
2    def countDigits(self, num: int) -> int:
3        count = 0
4        for c in str(num):
5            if num % int(c) == 0:
6             count += 1
7        return count 