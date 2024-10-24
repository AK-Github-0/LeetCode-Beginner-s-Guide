class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        wealth = 0
        for i in range(len(accounts)):
            if wealth < sum(accounts[i]):
                wealth = sum(accounts[i])

        return wealth
