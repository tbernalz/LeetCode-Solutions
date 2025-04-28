# Identify the Largest Outlier in an Array

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/description/).

## Initial Approach

My initial approach was to was based on iterating through **all possible pairs** of numbers in the input array and checking if removing two numbers leaves the sum of the remaining numbers equal to one of the removed numbers.

Here's how it worked:

1. **Understand the Problem**: The array contains `n−2` special numbers, 1 sum element (equal to the sum of all the special numbers), and 1 outlier. The task is to identify the largest outlier.

1. **Brute-Force Approach**:

   - Iterate over all pairs of numbers `(i,j)` in the array.

   - For each pair, calculate the "target" sum as: `target = total_sum − nums[i] − nums[j]`

   - If the target equals one of the removed numbers, the other number in the pair is a candidate for the outlier.

   - Update the largest outlier found so far.

1. **Why It Worked**:

   - By testing all possible pairs, the algorithm ensures that any valid combination of the sum element and the outlier is covered.

   - This guarantees correctness but is inefficient due to the `O(n^2)` pairwise iteration.

```Python
class Solution:
    def getLargestOutlier(self, nums: list[int]) -> int:
        """
        Given an array that contains n elements, where exactly n - 2 elements are special numbers. One of the remaining two elements is the sum of these special numbers, and the other is an outlier.
        An outlier is defined as a number that is neither one of the original special numbers nor the element representing the sum of those numbers.

        Args:
            nums(list[int]): The array to analyze.

        Returns:
            int: The largest potential outlier in nums.
        """
        total_sum = sum(nums)
        largest_outlier = float("-inf")

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                target = total_sum - nums[i] - nums[j]
                if target == nums[i]:
                    largest_outlier = max(largest_outlier, nums[j])

                elif target == nums[j]:
                    largest_outlier = max(largest_outlier, nums[i])

        return largest_outlier

```

## Optimized Solution

After analyzing the problem in-depth, and researching on LeetCode discussions, I discovered a more efficient approach to finding the largest outlier by leveraging `mathematical relationships` and using a set (`hash map`) for efficient lookups.

Here's how I arrived at the optimized solution:

1. **Key Insight: Relationship Between Sum and Outlier**:

   - The array contains **n−2 special numbers**, a **sum element** (equal to the sum of the special numbers), and an **outlier**.

   - The total sum of the array can be expressed as: `total_sum = 2 × sum_element + outlier`

   - Rearranging this equation, the `outlier` can be calculated for any number num treated as the sum element: `outlier = total_sum − 2 × num`

1. **Efficient Lookup with a Set**:

   - To quickly verify if the calculated outlier exists in the array, use a `set` (a `hash map` in Python), which provides `O(1)` average-time lookups.

   - This eliminates the need for nested loops and allows us to check conditions efficiently.

1. **Validation**:

   - Ensure that the `outlier` is a valid number in the array by:

     - Checking its presence in the set.

     - Handling duplicates carefully (e.g., ensuring the count of the number is sufficient).

1. **Why This is Better**:

   - The optimized solution avoids nested loops, reducing time complexity from `O(n^2)` to `O(n)`.

   - It uses concise and efficient **mathematical calculations**, combined with a **hash map** for lookups, to handle the problem in linear time.

## Complexity

**Initial Approach**:

- **Time Complexity**: `O(n^2)`, where n is the length of the array.

- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.

**Optimized Solution**:

- **Time Complexity**: `O(n))`, where n is the length of the array.

  - The single loop iterates through the array, performing O(1) calculations for each element and O(n) for the total.

- **Space Complexity**: `O(n)`, A set is used to store the elements of the array for efficient lookups.
