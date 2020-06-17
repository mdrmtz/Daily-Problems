# You are given a list of numbers, and a target number k. Return whether or not there are two numbers in the list that add up to k.

Example:
* Given [4, 7, 1 , -3, 2] and k = 5,
  return true since 4 + 1 = 5.
  
```python
def two_sum(list, k):
  for n in list:
      if k-n in list:
          return True
      
  return False

print two_sum([4,7,1,-3,2], 5)
# True
```
