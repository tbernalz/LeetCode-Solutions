# Happy Number 

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/happy-number/description/).

## Initial Approach
In my first solution, I used a hash map to track previously seen results. For each number, I calculated the sum of the squares of its digits and checked if this result already existed in the hash map:

* If the result was 1, it means the number is a happy number, so I returned `True`.
* If the result was **not** in the hash map, I added it and continued the process.
* If the result was **already** in the hash map, it meant we had entered a cycle, so I returned `False`.

``` Python
class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Define if a number is happy based on some rules

        Args:
            n(int): The number to check

        Returns:
            bool: True if the number is happy, False otherwise
        """
        hash_results = {}

        while n not in hash_results:
            hash_results[n] = True
            n = sum(int(digit) ** 2 for digit in str(n))

            if n == 1:
                return True

        return False

```

## Optimized Solution
Later, I learned about **Floyd's Cycle-Finding Algorithm** (also known as the "Hare-Tortoise Algorithm") and realized that I could optimize my solution. By using two pointers (`slow` and `fast`), I could detect cycles without requiring extra space for a hash map.

Here’s how it works:

1. Use one pointer (slow) that moves one step at a time and another pointer (`fast`) that moves two steps at a time.
1. If there is a cycle, the two pointers will eventually meet.
1. If the `fast` pointer reaches 1, the number is happy, and the function returns `True`.

This optimization maintains the same time complexity but significantly reduces space complexity.

## Complexity

**Initial Approach**:
* **Time Complexity**: `O(log n),`, where n is the input number.
* **Space Complexity**: `O(243)`, as the hash map stores at most 243 entries.

**Optimized Solution**:
* **Time Complexity**: `O(log n),`, where n is the input number.
* **Space Complexity**: `O(1)`, since no additional storage is needed beyond a few variables for the pointers.grow up to n calls.
