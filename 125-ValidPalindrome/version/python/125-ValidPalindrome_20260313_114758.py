# Last updated: 3/13/2026, 11:47:58 AM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        stack = []
4
5        for ch in s:
6            if ch.isalnum():
7                stack.append(ch.lower())
8
9        return stack==stack[::-1]
10        