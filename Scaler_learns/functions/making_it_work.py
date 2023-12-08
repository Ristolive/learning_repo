def my_min(*nums):
    min = nums[0]
    for x in nums:
        if x<min:
            min=x
    return min
print(my_min(8,13,4,42,120,7))