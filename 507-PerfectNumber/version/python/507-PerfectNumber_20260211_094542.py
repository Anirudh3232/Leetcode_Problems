# Last updated: 2/11/2026, 9:45:42 AM
1class Solution:
2    def checkPerfectNumber(self, num: int) -> bool:
3        if num <= 1:
4            return False
5
6        division_sum = 1
7
8        i = 2
9        while i * i <= num:
10           if num % i == 0:
11             division_sum += i
12             patner = num // i
13            
14             if patner != i and patner != num:
15                  division_sum += patner
16
17           i += 1
18       
19        return division_sum == num
20
21
22