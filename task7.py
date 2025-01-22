def has_33(nums):
    for num in nums:
        if nums[0] == nums [1] == 3 or nums[1] == nums[2] == 3:
            return True
        else:
            return False
nums_string = input()
nums = list(map(int, nums_string.split()))
print(has_33(nums))