# Maximum Split of Positive Even Integers

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/maximum-split-of-positive-even-integers/description/).

## Initial Approach

The initial approach employs a greedy strategy with these steps:

1. **Input Check**: The code first checks if `finalSum` is odd. If it is, no split into even numbers is possible, and an empty list is immediately returned.

2. **Greedy Selection**: The algorithm iteratively adds the smallest unique positive even numbers (2, 4, 6, 8, ...) to the `result` list and updates `current_sum`.

3. **Exact Match**: If `current_sum` equals `finalSum`, the current `result` is returned as it contains the maximum number of terms by using the smallest possible ones.

4. Overshoot Correction: If `current_sum` exceeds `finalSum`, it means the last added number (`overshoot_num`) caused the sum to be too large.

   - This last number is removed from the `result` and subtracted from `current_sum`.

   - The remaining difference, `remainder` ($= finalSum - current\_sum$), must be added to one of the existing numbers in `result` to reach `finalSum`.

   - Crucially, to maintain the uniqueness of the numbers, the `remainder` is added to the largest remaining element in the list, `result[-1]`. Since all the numbers added so far are the smallest consecutive evens, the `remainder` (which is itself an even number, calculated as $finalSum - (2 + 4 + \dots + (N-2))$) is guaranteed to be large enough to ensure the updated $result[-1] + remainder$ remains unique and greater than all other elements.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(√n)`, where n is the `finalSum` given.

- **Space Complexity**: `O(√n)`, where n is the `finalSum` given.
