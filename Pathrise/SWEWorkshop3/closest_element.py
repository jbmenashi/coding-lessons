def find_nearest(arr, target):
   left = 0
   right = len(arr) - 1
   while left + 1 < right: # so that the two variables don't overlap, which could cause a crash
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    #Post Processing
    if abs(target - arr[left]) <= abs(target - arr[right]):
        return left
    else:
        return right


find_nearest([1, 2, 3, 6, 7], 4)
