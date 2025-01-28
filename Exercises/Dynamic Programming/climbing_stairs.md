# Climbing Stairs

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/climbing-stairs/description/?source=submission-ac).

## Initial Approach

When solving the problem by hand for the first five steps, I noticed a pattern resembling the Fibonacci sequence:
* `n = 1` → 1 ways
* `n = 2` → 2 ways
* `n = 3` → 3 ways
* `n = 4` → 5 ways
* `n = 5` → 8 ways

However, the problem is not a perfect Fibonacci sequence because when `n = 2`, the result is `2` instead of `1`. This discrepancy occurs because the base cases differ slightly: the result for this problem aligns with `fibonacci(n + 1)` when `n != 0`.

## Optimized Solution

Initially, the solution was implemented without caching, which led to inefficient performance. Upon reviewing a forum discussion, I discovered the concept of memoization (caching). The initial algorithm recalculated the same subproblems multiple times, leading to redundant computations and wasted resources.

By introducing caching, the solution saves the results of previously solved subproblems in a dictionary. This optimization significantly improves performance by avoiding repeated calculations, thereby reducing the time complexity from exponential (`O(2^n)`) to linear (`O(n)`). Additionally, it minimizes the computational overhead, making the algorithm more efficient and scalable.

## Complexity

**Initial Approach**:
* **Time Complexity**: `O(2^n)`, where n is the number of stairs to climb.
* **Space Complexity**: `O(n)`, as the maximum depth of the recursion stack is n due to the recursive calls for each subproblem.

**Optimized Solution**:
* **Time Complexity**: `O(n)`, where n is the number of stairs to climb.
* **Space Complexity**: `O(n)`, as the cache stores the results of all subproblems, and the recursion stack can grow up to n calls.
