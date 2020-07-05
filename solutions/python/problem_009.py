def single_number(nums):
    result = 0
    for item in nums:
        result ^= item

    return result


# 1
print(single_number([4, 3, 2, 4, 1, 3, 2]))
assert single_number([4, 3, 2, 4, 1, 3, 2]) == 1
