# Number of Unique XOR Triplets I

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/number-of-unique-xor-triplets-i/description/).

## Initial Approach

The initial approach is a brute force method that checks all possible triplets `(i, j, k)` where `i <= j <= k` and computes their XOR values. These values are stored in a set to ensure uniqueness. Finally, the size of the set is returned, representing the number of unique XOR triplet values.

This approach is straightforward but highly inefficient, especially for larger arrays, as it involves three nested loops leading to a time complexity of `O(n^3)`. The space complexity is also high due to the storage of all unique XOR values.

```Python
from typing import List


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        xor_unique_values = set()

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                for k in range(j, len(nums)):
                    xor_unique_values.add(nums[i] ^ nums[j] ^ nums[k])

        return len(xor_unique_values)

```

## Optimized Solution

After brute-forcing small test cases, I discovered a clear power-of-two pattern between the array length (`n`) and the number of unique XOR triplets.

The number of unique XOR triplets is exactly `2^m`, where `m` is the number of bits needed to represent `n` in binary.

## Complexity

**Initial Approach**:

- **Time Complexity**: `O(n^3)`, where n is the length of the array.

- **Space Complexity**: `O(n^3)`, since in the worst case all the results are different and we store all of them.

**Optimized Solution**:

- **Time Complexity**: `O(log n)`, where n is the length of the array.

- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.
