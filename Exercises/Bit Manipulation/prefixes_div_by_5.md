## Binary Prefix Divisible By 5

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/binary-prefix-divisible-by-5/).

## Initial Approach

In my solution I avoid directly converting binary to decimal for every prefix, which could be inefficient. Instead, I used a rolling calculation to keep track of the decimal value of the binary prefixes modulo 5 (divided by 5). Starting with `current_number = 0`, each new bit in the array updates the number like this:

1. Shift the current value left (multiply by 2) to make room for the new bit.

1. Add the new bit (`num`) to the value.

1. Take the result `modulo 5` to simplify and prevent the number from growing too large.

At each step, we check if the current value is divisible by 5 by comparing `current_number % 5 == 0`. This result is stored in the `answer` array. The process is efficient, and we iterate over the binary array just once.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n)`, where n is the length of the `nums` array.

- **Space Complexity**: `O(n)`, where n is the length of the `answear` array, which has the same length as the `nums` one.
