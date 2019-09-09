def getPeak(nums):  # [1,2,1,3,5,6,4]
    l = 0
    r = len(nums) - 1  # r is 6
    while l + 1 < r:
        mid = (l + r) // 2  # mid is 3
        # 3 is greater than 1, 3 is NOT greater than 5
        if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
            return mid
        elif nums[mid] < nums[mid - 1]:  # 3 is NOT lesser than 1
            return mid - 1
        else:  # 3 IS lesser than 5
            l = mid
    if nums[r] > nums[l]:
        return r
    if nums[l] > nums[r]:
        return l
