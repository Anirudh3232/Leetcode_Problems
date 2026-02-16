# Last updated: 2/16/2026, 7:41:32 AM
1class Solution:
2    def countPrimes(self, n: int) -> int:
3        if n <= 2 :
4            return 0 
5
6        is_prime = [True] * n
7
8        is_prime[0] = is_prime[1] = False
9
10        for p in range(2, int(n**0.5) + 1):
11            if is_prime[p]:
12                for multiple in range(p * p, n, p):
13                    is_prime[multiple] = False
14        return sum(is_prime)
15
16
17                     
18
19