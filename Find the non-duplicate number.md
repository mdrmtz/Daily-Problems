# Given a list of numbers, where every number shows up twice except for one number, find that one number.

Example:
* Input: [4, 3, 2, 4, 1, 3, 2]
* Output: 1
```python
def singleNumber(nums):
    result = 0
    for item in nums:
      result ^=item
      print(result)
      
    return result

print singleNumber([4, 3, 2, 4, 1, 3, 2])
# 1
```
