def sort_nums(nums):
    a = 0
    b = 0
    c = 0
    for n in nums:
        if n == 1:
            a += 1
        elif n == 2:
            b += 1
        else:
            c += 1

    return [1] * a + [2] * b + [3] * c


print(sort_nums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]
assert sort_nums([3, 3, 2, 1, 3, 2, 1]) == [1, 1, 2, 2, 3, 3, 3]
