def remove_duplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1


# Example usage:
nums = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6]

n = remove_duplicates(nums)

print("Array after removing duplicates:", nums[:n])


def remove_duplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1

# Example usage:
nums = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6]

n = remove_duplicates(nums)

print("Array after removing duplicates:", nums[:n])

