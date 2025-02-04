# Maximum Sum of Distinct Subarrays With Length K

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/).

## Initial Approach

In my initial approach, I recognized that the problem of finding the maximum subarray sum of size `k` with distinct elements can be efficiently solved using the `Sliding Window Technique`:

1. **Sliding Window Concept**:

   - I used a **window of size k** that dynamically expands and contracts while maintaining a **set** to ensure element uniqueness.

   - The right pointer (`right`) expands the window, while the left pointer (`left`) shrinks it when duplicates appear.

1. Handling Duplicates:

   - If `nums[right]` is already in the **set**, I remove elements from the left until it becomes unique.

   - This ensures that every subarray considered maintains distinct elements.

1. Maximizing the Sum:

   - Whenever the window reaches the required size `k`, I update `max_sum` if the current sum is greater.

   - Before moving forward, I remove the leftmost element to slide the window.

This approach efficiently ensures that every valid subarray is considered while maintaining distinct elements using a **set**.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n)`, where n is the length of the array `nums`.

- **Space Complexity**: `O(k)`, where k is the subarray length.
