# Intuition
The problem asks for the minimum number of steps to reduce a number to zero. If the number is even, you can divide it by 2; if it's odd, you subtract 1. This suggests a straightforward approach using a loop until the number becomes zero.

# Approach
- Initialize a counter `steps` to keep track of the number of operations.
- Use a `while` loop that runs until `num` is reduced to 0.
  - If `num` is even, divide it by 2.
  - If `num` is odd, subtract 1 from it.
- Increment the `steps` counter after each operation.
- Return the number of steps after the loop finishes.

# Complexity
- **Time complexity**: $$O(\log n)$$  
  The number of steps required is proportional to the number of bits in the binary representation of `num`. In the worst case, this is approximately the number of times you can divide `num` by 2 (logarithmic complexity).

- **Space complexity**: $$O(1)$$  
  I only use a constant amount of extra space to store the number of steps.

# Code
```python
class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        steps = 0
        while num != 0:
            if num % 2 == 0:
                num = num / 2
            else:
                num -= 1
            steps += 1
        return steps
```
