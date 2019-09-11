def searchRange(nums, target):
  l = 0
  r = len(nums) - 1
  while l + 1 < r:
    mid = (l + r) // 2
    print(mid)
    if nums[mid] == target:
      while nums[l] != target:
        l = l + 1
      while nums[r] != target:
        r = r - 1
      return [l, r]
    elif nums[mid] < target:
      l = mid + 1
    else:
      r = mid - 1
  return [-1, -1]
