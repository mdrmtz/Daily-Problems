# Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.

Example 1:
* Input: [3, 3, 2, 1, 3, 2, 1]
* Output: [1, 1, 2, 2, 3, 3, 3]

# Solution 1

```python
def sortNums(nums):
  a = 0
  b = 0
  c = 0
  for n in nums:
      if n == 1:
          a+=1
      elif n == 2:
          b+=1
      else:
          c+=1
     
  return [1] * a + [2] * b + [3] * c

print sortNums([3, 3, 2, 1, 3, 2, 1])
# [1, 1, 2, 2, 3, 3, 3]
```
# Solution 2
```python
def sortNums(nums):
  leftmost_index = 0 # Represents the leftmost index
  rightmost_index = len(nums) - 1 # Represents the rightmost index
  current_index = 0 # Index that we are checking
  while current_index <= rightmost_index:
    if nums[current_index] == 1:
      # Swap numbers with leftmost index
      nums[current_index], nums[leftmost_index] = nums[leftmost_index], nums[current_index]
      current_index += 1
      leftmost_index += 1
    elif nums[current_index] == 2:
      # If index is 2, it means list is in order, check next number
      current_index += 1
    elif nums[current_index] == 3:
      # Swap numbers with rightmost index
      nums[current_index], nums[rightmost_index] = nums[rightmost_index], nums[current_index]
      rightmost_index -= 1
  return nums

print sortNums([3, 3, 2, 1, 3, 2, 1])
# [1, 1, 2, 2, 3, 3, 3]
```
