# Last updated: 3/8/2026, 9:21:22 AM
1class Solution:
2    def reverseStr(self, s: str, k: int) -> str:
3
4        s = list(s)
5
6        for i in range(0, len(s), 2*k):
7            s[i:i+k] = reversed(s[i:i+k])
8
9        return "".join(s)
10        