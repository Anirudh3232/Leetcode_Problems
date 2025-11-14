# Last updated: 11/14/2025, 8:47:55 AM
class Solution:
    def maximumWealth(self, accounts):
        return max(sum(customer) for customer in accounts)
