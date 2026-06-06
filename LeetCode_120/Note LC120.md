# LeetCode #1 - Two Sum

## Pattern

**Hash Map / Dictionary Lookup**

## Key Idea

For each number:

1. Calculate the number needed to reach the target.
2. Check if that number has already been seen.
3. If yes, return the two indices.
4. If no, store the current number and its index.

## Template

```python
def twoSum(nums, target):
    check = {}

    for i in range(len(nums)):
        left = target - nums[i]

        if left in check:
            return [check[left], i]

        check[nums[i]] = i
```

## Why It Works

Example:

```python
nums = [2,7,11,15]
target = 9
```

Iteration 1:

```python
2
need = 7
```

7 not found.

Store:

```python
{2: 0}
```

Iteration 2:

```python
7
need = 2
```

2 found in dictionary.

Return:

```python
[0,1]
```

## Important Understanding

The dictionary stores numbers from **previous iterations**.

```python
check[nums[i]] = i
```

adds the current number and index to memory.

The dictionary is NOT reset every loop.

## Interview Takeaway

When solving a problem:

```text
Need a value?
↓
Have I seen it before?
↓
Use a Hash Map.
```

## Complexity

Time: O(n)

Space: O(n)

# LC #217 - Contains Duplicate

### Problem

Given an integer array `nums`, return `True` if any value appears at least twice in the array, and `False` if every element is distinct.

---

## Method 1: Set (Recommended)

### Key Idea

`set()` automatically removes duplicates.

```python
def containsDuplicate(nums):
    return len(nums) != len(set(nums))
```

### Example

```python
nums = [1, 2, 3, 1]
```

```python
set(nums)
```

returns

```python
{1, 2, 3}
```

Length comparison:

```python
len(nums)      = 4
len(set(nums)) = 3
```

Since the lengths are different:

```python
return True
```

### Pattern

```text
Need to know whether an element exists?
→ Use Set
```

---

## Method 2: Sort

### Key Idea

After sorting, duplicates become adjacent.

```python
nums = [1, 2, 3, 1]
```

Sort:

```python
[1, 1, 2, 3]
```

Check neighboring elements:

```python
1 == 1
```

Duplicate found.

```python
def containsDuplicate(nums):
    nums.sort()

    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True

    return False
```

---

# LC #242 - Valid Anagram

### Problem

Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`.

An anagram contains exactly the same letters with the same frequencies.

---

## Method 1: Sort (Recommended)

### Key Idea

If two words are anagrams, their sorted forms are identical.

```python
s = "eat"
t = "tea"
```

```python
sorted(s)
```

returns

```python
['a', 'e', 't']
```

```python
sorted(t)
```

returns

```python
['a', 'e', 't']
```

Compare:

```python
sorted(s) == sorted(t)
```

returns

```python
True
```

### Solution

```python
def isAnagram(s, t):
    return sorted(s) == sorted(t)
```

---

## Method 2: Counter

### Counter

`Counter()` is a built-in class from the `collections` module.

```python
from collections import Counter
```

Purpose:

```text
Automatically count frequencies.
```

Example:

```python
Counter("banana")
```

returns

```python
{
    'a': 3,
    'n': 2,
    'b': 1
}
```

### Solution

```python
from collections import Counter

def isAnagram(s, t):
    return Counter(s) == Counter(t)
```

---

# Join Function Notes

### General Form

```python
separator.join(list_of_strings)
```

The separator is inserted between every element.

---

### Example 1

```python
letters = ['a', 'e', 't']

"".join(letters)
```

returns

```python
"aet"
```

Meaning:

```text
Join with nothing between elements.
```

---

### Example 2

```python
letters = ['a', 'e', 't']

" ".join(letters)
```

returns

```python
"a e t"
```

Meaning:

```text
Join with a space between elements.
```

---

### Example 3

```python
letters = ['a', 'e', 't']

"-".join(letters)
```

returns

```python
"a-e-t"
```

Meaning:

```text
Join with a dash between elements.
```

---

# Important Distinction

## set()

```python
set([1,1,2,2,3])
```

returns

```python
{1,2,3}
```

Purpose:

```text
Check existence.
Remove duplicates.
```

---

## dict()

```python
{
    "name": "Hao"
}
```

Purpose:

```text
Store key-value pairs.
```

---

## Counter()

```python
Counter([1,1,2,2,2,3])
```

returns

```python
{
    1: 2,
    2: 3,
    3: 1
}
```

Purpose:

```text
Count frequencies.
```

# LC #347 - Top K Frequent Elements

## Problem

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.

Example:

```python
nums = [1,1,1,2,2,3]
k = 2
```

Output:

```python
[1,2]
```

Because:

```text
1 appears 3 times
2 appears 2 times
3 appears 1 time
```

---

# Key Pattern

```text
Count Frequency
→ Sort by Frequency
→ Return Top K
```

This is a HashMap + Sorting problem.

---

# Step 1 - Count Frequencies

Use a dictionary.

```python
count = {}

for num in nums:
    if num not in count:
        count[num] = 1
    else:
        count[num] += 1
```

Example:

```python
nums = [1,1,1,2,2,3]
```

Result:

```python
{
    1: 3,
    2: 2,
    3: 1
}
```

Meaning:

```text
key   = number
value = frequency
```

---

# Step 2 - Sort By Frequency

Dictionary items:

```python
count.items()
```

Result:

```python
[
    (1,3),
    (2,2),
    (3,1)
]
```

Each tuple:

```python
(number, frequency)
```

Helper function:

```python
def get_frequency(item):
    return item[1]
```

Sort:

```python
sorted_items = sorted(
    count.items(),
    key=get_frequency,
    reverse=True
)
```

Result:

```python
[
    (1,3),
    (2,2),
    (3,1)
]
```

---

# Step 3 - Get Top K

Example:

```python
k = 2
```

Take first k elements:

```python
sorted_items[:k]
```

Result:

```python
[
    (1,3),
    (2,2)
]
```

---

# Step 4 - Extract Numbers

```python
result = []

for num, freq in sorted_items[:k]:
    result.append(num)

return result
```

Result:

```python
[1,2]
```

---

# Full Solution

```python
class Solution:
    def topKFrequent(self, nums, k):

        count = {}

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        def get_frequency(item):
            return item[1]

        sorted_items = sorted(
            count.items(),
            key=get_frequency,
            reverse=True
        )

        result = []

        for num, freq in sorted_items[:k]:
            result.append(num)

        return result
```

---

# Complexity

Frequency Count:

```text
O(n)
```

Sorting:

```text
O(m log m)
```

where:

```text
m = number of unique elements
```

Overall:

```text
O(n log n)
```

---

# Takeaways

## Dictionary

```python
count[num] += 1
```

Purpose:

```text
Count frequencies
```

---

## items()

```python
count.items()
```

Returns:

```python
(key, value)
```

Example:

```python
(1,3)
```

Meaning:

```text
number = 1
frequency = 3
```

---

## Sort by Value

```python
sorted(
    count.items(),
    key=get_frequency,
    reverse=True
)
```

Purpose:

```text
Sort by frequency from largest to smallest.
```

---

# LeetCode 238 - Product of Array Except Self

## Pattern

Prefix Product + Suffix Product

---

## Recognition

When a problem asks:

```text
For each index,
use all elements except itself.
```

Think:

```text
Prefix + Suffix
```

---

## Prefix Pass

```python
ans[i] = pre
pre *= nums[i]
```

Meaning:

```text
Store first.
Update later.
```

`ans[i]` should contain the product of everything BEFORE index i.

Example:

```python
nums = [1,2,3,4]
```

After prefix pass:

```python
ans = [1,1,2,6]
```

---

## Suffix Pass

```python
ans[i] *= pos
pos *= nums[i]
```

Meaning:

```text
Use current suffix first.
Then update suffix.
```

`pos` stores the product of everything to the RIGHT.

Example:

```python
i = 2

ans[2] = 2
pos = 4

ans[2] *= pos
```

Result:

```python
8
```

because:

```text
left product  = 1×2 = 2
right product = 4

2 × 4 = 8
```

---

## Important Insight

Correct:

```python
ans[i] *= pos
pos *= nums[i]
```

Wrong:

```python
pos *= nums[i]
ans[i] *= pos
```

Why?

Because the current element would be included in its own product.

---

## Reverse Loop

Correct:

```python
for i in range(len(nums)-1, -1, -1):
```

Remember:

```text
len(nums)
=
first invalid index

len(nums)-1
=
last valid index
```

---

## Final Template

```python
ans = [1] * len(nums)

pre = 1
for i in range(len(nums)):
    ans[i] = pre
    pre *= nums[i]

pos = 1
for i in range(len(nums)-1, -1, -1):
    ans[i] *= pos
    pos *= nums[i]

return ans
```

---

## Biggest Lesson

I understood the pattern before I understood the code.

The challenge was translating:

```text
"product of everything on the left"
```

into

```python
ans[i] = pre
pre *= nums[i]
```

and

```text
"product of everything on the right"
```

into

```python
ans[i] *= pos
pos *= nums[i]
```

The key idea:

```text
Store first.
Update later.
```

# LeetCode 36 - Valid Sudoku

## Pattern
Hash Set + Matrix Traversal

## Key Takeaway

The problem is NOT asking us to solve Sudoku.

We only need to detect whether a number has already appeared in:

- the same row
- the same column
- the same 3×3 box

Use a Hash Set to record what has been seen.

Store three kinds of information:

(row, num)
(num, col)
(box_row, box_col, num)

If any of them already exist in the set:

return False

Otherwise add them into the set.

## Important Concept

Tuple can be used as a key inside a set.

Examples:

(0, "5")
→ Number 5 appeared in Row 0

("5", 0)
→ Number 5 appeared in Column 0

(0, 0, "5")
→ Number 5 appeared in Top-Left Box

## Box Calculation

(i // 3, j // 3)

Used to determine which 3×3 box the current cell belongs to.

## Common Mistakes

- Trying to solve the Sudoku
- Using "," instead of "."
- Returning True inside the loop
- Forgetting box validation

## Complexity

Time: O(1)

Space: O(1)