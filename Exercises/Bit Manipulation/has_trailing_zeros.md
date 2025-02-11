# Check if Bitwise OR Has Trailing Zeros

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/description/).

## Initial Approach

While working through some handwritten examples, I realized that a number will have at least one trailing zero in its binary representation if it is even. This is because an even number has at least one factor of 2, which corresponds to a trailing zero in binary. Therefore, the problem reduces to checking if there are at least two even numbers in the array.

The approach iterates through the array and counts the number of even numbers. If the count reaches two, it immediately returns True, indicating that there are at least two numbers whose bitwise OR will have a trailing zero. If the loop completes without finding two even numbers, it returns False.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n)`, where n is the length of the array.

- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.
