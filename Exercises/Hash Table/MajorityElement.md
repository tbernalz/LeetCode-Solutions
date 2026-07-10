# Majority Element

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/majority-element/description/).

## Initial Approach

The initial approach uses a frequency-counting strategy to identify the majority element. It starts by initializing a dictionary with unique keys from the input array, setting all initial counts to zero.

It then iterates through the entire `nums` array to count the occurrences of each number, storing the frequencies in the dictionary. Finally, a second loop traverses the dictionary to find the key with the highest count, which is guaranteed by the problem constraints to be the majority element appearing more than $n / 2$ times.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n)`, where n is the number of elements in the array.
- **Space Complexity**: `O(u)`, where u is the number of unique elements in the array.
