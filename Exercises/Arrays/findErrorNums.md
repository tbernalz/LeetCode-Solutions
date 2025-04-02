# Set Mismatch

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/set-mismatch/description/).

## Initial Approach

The initial approach involves sorting the array to group identical numbers together, making it easier to identify the duplicate. After sorting, we iterate through the array to find the duplicate number where `nums[i] == nums[i+1]`.

To find the missing number, we calculate the expected sum of numbers from `1` to `n` using the formula `n\*(n+1)/2`. The actual sum of the array is computed, and the missing number is derived by adjusting for the duplicate: `missing = expected_sum - (actual_sum - duplicate)`.

```Python
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        duplicate = -1
        expected_sum = len(nums) * (len(nums) + 1) // 2
        actual_sum = sum(nums)

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                duplicate = nums[i]
                break

        missing = expected_sum - (actual_sum - duplicate)

        return [duplicate, missing]

```

## Optimized Solution

The optimized solution leverages the array indices to mark the presence of numbers. For each number in the array, we use its absolute value as an index and negate the value at that index. If we encounter a negative value at an index, it means the corresponding number has been seen before, indicating the duplicate.

After marking, the index of the remaining positive value in the array gives the missing number. This approach efficiently finds both the duplicate and missing numbers in a single pass through the array, followed by another pass to identify the missing number.

## Complexity

**Initial Approach**:

- **Time Complexity**: `O(n log n)`, where n is the length of the array.

- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.

**Optimized Solution**:

- **Time Complexity**: `O(n)`, where n is the length of the array.

- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.
