# Maximum Length of Pair Chain

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/maximum-length-of-pair-chain/description/).

## Initial Approach

The initial approach involves sorting the pairs based on their end values. This allows us to greedily select the pair with the smallest end first, ensuring that we can fit as many subsequent pairs as possible into the chain.

After sorting, we initialize a counter to keep track of the length of the chain and a variable to store the end of the last pair added to the chain. We then iterate through the sorted pairs, and for each pair, if its start is greater than the end of the last pair in the chain, we increment the counter and update the end to the current pair's end.

This approach ensures that we always extend the chain with the pair that has the earliest possible end, maximizing the number of pairs we can include.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n log n)`, where n is the number of pairs.
  - The `O(n log n)` comes from the sorting step, which dominates the time complexity. The subsequent iteration through the pairs is `O(n)`, but the overall complexity is determined by the sorting.
- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.
