def searchInsert(nums, target):
    l = 0
    r = len(nums) - 1
    while l + 1 < r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid
        else:
            r = mid
    if target > nums[r]:
        return r + 1
    elif target < nums[r] and target > nums[l]:
        return r
    else:
        return l
