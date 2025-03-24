# Divide Array Into Equal Pairs

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/divide-array-into-equal-pairs/description/).

## Initial Approach

The initial approach involves using a hash set to track the occurrence of each number in the array. The idea is to iterate through each number in the array and check if it has been seen before (i.e., it exists in the set).

- If the number is already in the set, it means we’ve found a pair, so we remove it from the set.

- If the number is not in the set, we add it to the set, indicating we’re waiting for its pair.

After processing all numbers, if the set is empty, it means every number had a pair, and we return `True`. Otherwise, if any numbers remain in the set (indicating unpaired numbers), we return `False`.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n)`, where n is the number of elements in the array.

- **Space Complexity**: `O(n)`, where n is the number of elements in the array.
