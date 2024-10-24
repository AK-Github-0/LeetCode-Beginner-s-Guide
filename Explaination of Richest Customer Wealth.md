# Intuition
The problem asks to determine the maximum wealth a customer has, where the wealth is calculated as the sum of money in each bank account. The key is to compute the sum of each customer's accounts and return the maximum value.

# Approach
- Initialize a variable `wealth` to keep track of the maximum wealth.
- Iterate over each customer’s account, calculate the sum of their wealth, and update `wealth` if the current sum is greater than the previous maximum.
- Return the final value of `wealth`.

# Complexity
- **Time complexity**: $$O(m \times n)$$  
  Here, `m` is the number of customers and `n` is the number of accounts per customer. We iterate through each customer's accounts once to compute the sum.

- **Space complexity**: $$O(1)$$  
  We are only using a constant amount of extra space for storing `wealth`.

# Code
```python
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
```
