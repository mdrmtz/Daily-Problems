def sort_nums(nums):
    leftmost_index = 0  # Represents the leftmost index
    rightmost_index = len(nums) - 1  # Represents the rightmost index
    current_index = 0  # Index that we are checking
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


print(sort_nums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]

assert sort_nums([3, 3, 2, 1, 3, 2, 1]) == [1, 1, 2, 2, 3, 3, 3]
