# Last updated: 1/22/2026, 6:44:09 AM
1class Solution:
2    def romanToInt(self, s: str) -> int:
3
4
5       roman = { "I" : 1, "V" : 5, "X" : 10, 
6        "L" : 50, "C" : 100, "D" : 500, "M" : 1000 }
7       res = 0
8
9       for i in range(len(s)):
10           if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
11               res -= roman[s[i]]
12           else:
13               res += roman[s[i]] 
14       return res 