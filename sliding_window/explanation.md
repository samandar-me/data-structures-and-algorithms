The variable-size sliding window (also called an expandable/shrinkable window) is a technique for solving array and string problems where the window's length can change depending on a condition.

The core idea is:

- Expand the window by moving `right` to include more elements.
- Shrink the window by moving `left` to remove elements.
- Keep track of information about the current window instead of recalculating everything from scratch.

Let's learn it step by step.

## 1. The basic idea

Imagine this array:

```
nums = [2, 1, 5, 1, 3, 2]
```

Suppose the task is:

Find the shortest contiguous subarray whose sum is at least 7.

The window is the section between `left` and `right`, inclusive.

### Explore the window

Step 1 of 9

Window sum

# 2

Window length

# 1

Start with the first element. The sum is 2, which is less than 7, so expand.

PreviousNext step

Green cells belong to the current window. Indices are shown underneath each value.

The window starts small, grows until the condition is satisfied, and then shrinks to see whether a smaller valid window exists.

## 2. The standard template

This is the most important pattern to recognize:

```
left = 0
window_state = 0  # e.g. sum, count, or frequency map
result = ...

for right in range(len(nums)):
    # 1. Expand: include nums[right]
    window_state += nums[right]

    # 2. Shrink while the window satisfies the condition
    while condition(window_state):
        # 3. Update the answer
        result = ...

        # 4. Remove nums[left] and shrink
        window_state -= nums[left]
        left += 1
```

The exact operations depend on the problem. For a frequency map, you increment and decrement counts rather than adding and subtracting numbers.

Notice the difference between `if` and `while`:

- `if` shrinks the window at most once.
- `while` keeps shrinking as long as the condition remains satisfied.

For problems seeking the shortest valid window, `while` is often crucial because several consecutive left-side elements may be removable while the window stays valid.

## 3. Example: shortest subarray with sum at least 7

Here's a complete implementation for positive integers:

```
def min_subarray_len(target, nums):
    left = 0
    window_sum = 0
    min_length = float("inf")

    for right in range(len(nums)):
        window_sum += nums[right]

        while window_sum >= target:
            min_length = min(min_length, right - left + 1)

            window_sum -= nums[left]
            left += 1

    return 0 if min_length == float("inf") else min_length
```

For:

```
nums = [2, 1, 5, 1, 3, 2]target = 7
```

The answer is `2`, because the subarray `[5, 1, 3]` has sum 9 and length 3, but `[5, 1, 3]` isn't length 2; the actual shortest valid subarray is `[5, 1, 3]`? Let's check the array carefully: the pair `[5, 1]` sums to 6, `[1, 3]` sums to 4, and `[3, 2]` sums to 5. Thus no pair reaches 7, and the correct answer is 3.

## 4. How do you know when to expand or shrink?

This is where the problem statement matters.

| Goal                                            | Typical approach                                 |
| ----------------------------------------------- | ------------------------------------------------ |
| Find the shortest window satisfying a condition | Expand; when valid, record the answer and shrink |
| Find the longest window satisfying a condition  | Expand; while invalid, shrink; update the answer |
| Count windows satisfying a condition            | Often requires a specialized counting strategy   |
| Find a permutation/anagram in a string          | Fixed-size window with character frequencies     |

One critical limitation: the sum-based example relies on positive numbers. If negative numbers are allowed, expanding the window doesn't necessarily increase the sum, and shrinking doesn't necessarily decrease it. The usual sliding-window logic may then fail.

## 5. Complexity

For the standard two-pointer pattern:

- Time: \\(O(n)\\), when each pointer only moves forward. Even though there's a nested `while` loop, `left` advances at most \\(n\\) times in total.
- Space: \\(O(1)\\) auxiliary space when tracking a constant number of variables; \\(O(k)\\) if maintaining a frequency map of up to \\(k\\) distinct elements.

The trick is to avoid moving either pointer backward. Each element enters the window once and leaves at most once.

## 6. Test your understanding

Suppose you want the longest substring without repeating characters, a classic LeetCode problem.

For `"abcabcbb"`:

- You expand the window while characters are unique.
- When a duplicate appears, you shrink from the left until the duplicate is removed.
- You track the longest valid window.

When should you shrink the window in this problem?

Every time `right` moves.

Only when the window contains a duplicate, continuing until it becomes valid.

Only when the window reaches the end of the string.

Correct. Expand freely, then shrink while the window is invalid.

Once you understand which condition makes a window valid or invalid, choosing when to expand and shrink becomes much easier.