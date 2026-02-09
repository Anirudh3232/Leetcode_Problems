# Last updated: 2/8/2026, 6:54:49 PM
1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3
4        if x < 0:
5            return False
6        
7        if x == 0:
8            return True
9
10        div = 1
11        while x >= 10 * div:
12            div *= 10
13
14        while x:
15            left = x // div    
16            right = x % 10     
17
18            if left != right:
19                return False
20            x = (x % div) // 10
21            div //= 100
22        return True
23