# Intuition
The goal of the problem is to calculate a running sum of the input list. This can be done efficiently by iterating over the list once and maintaining a cumulative sum.

# Approach
- Initialize a variable `num` to store the cumulative sum.
- Iterate through the list `nums`, adding each element to `num` and appending the result to a new list `l`.
- Return the list `l` which contains the running sum at each index.

# Complexity
- **Time complexity**: $$O(n)$$  
  We traverse the input list `nums` once, where `n` is the length of the list.

- **Space complexity**: $$O(n)$$  
  We use a new list `l` to store the running sum, which has the same size as the input list.

# Code
```python
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num = 0
        l = []
        for i in range(len(nums)):
            num += nums[i]
            l.append(num)
        return l
```

