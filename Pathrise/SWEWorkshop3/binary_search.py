def binarySearch(arr, target):
   l = 0
   r = len(arr) - 1
   while l <= r:
      mid = (l + r) / 2
      if target == arr[mid]:
         return mid
      elif target > arr[mid]:
         l = mid + 1
      else:
         r = mid - 1
   return -1