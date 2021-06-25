# for loop

"""
for item in iterable_object 
  # do something with item 
"""

# for num in range(10):
#     print(num)

# while loop: while boolean -> condition


def two_sum(nums, target):
    left_idx, right_idx = 0, len(nums) - 1
    while left_idx < right_idx:
        sum = nums[left_idx] + nums[right_idx]
        if sum == target:
            return [nums[left_idx], nums[right_idx]]
        elif sum > target:
            right_idx -= 1
        else:
            left_idx += 1
        # end of loop
    return -1


# end of function


nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))
