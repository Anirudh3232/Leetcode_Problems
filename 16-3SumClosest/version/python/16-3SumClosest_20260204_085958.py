# Last updated: 2/4/2026, 8:59:58 AM
1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3
4       if  len(haystack) < len(needle):
5            return -1
6
7       for i in range(len(haystack)- len(needle) + 1):
8           if haystack[i: i+len(needle)] == needle:
9                return i
10      
11       return -1
12