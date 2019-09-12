def searchRange(nums, target):
   l = 0
   r = len(nums) - 1
   while l <= r:
      mid = (l + r) // 2
      if nums[mid] == target:
         l = mid
         r = mid
         while nums[l - 1] == target:
            l = l - 1
         while nums[r + 1] == target:
            r = r + 1
         return [l, r]
      elif nums[mid] < target:
         l = mid + 1
      else:
         r = mid - 1
   return [-1, -1]
