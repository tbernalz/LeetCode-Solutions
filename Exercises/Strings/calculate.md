# Basic Calculator II

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/basic-calculator-ii/description/).

## Initial Approach

The initial approach involves processing the string expression while handling different operations (`+`, `-`, `*`, `/`) with proper precedence. The algorithm uses a stack to keep track of intermediate results, ensuring that multiplication and division are performed immediately, while addition and subtraction are deferred until the end.

1. **Iterate through the string**: Parse each character, accumulating numbers until an operator or the end of the string is encountered.

1. **Handle operations**:

   - If the operation is `+` or `-`, push the number (with appropriate sign) onto the stack.

   - If the operation is `*` or `/`, pop the last value from the stack, perform the operation, and push the result back.

1. **Sum the stack**: After processing all characters, the stack contains numbers that can be summed to get the final result.

This approach ensures correct operator precedence by deferring addition and subtraction while immediately resolving multiplication and division.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n)`, where n is the length of the string.
- **Space Complexity**: `O(n)`, where n is the length of the string.
