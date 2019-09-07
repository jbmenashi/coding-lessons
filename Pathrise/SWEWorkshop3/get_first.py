def get_first(arr, target):
    l, r = 0, len(arr) - 1
    while l + 1 < r:
        mid = l + (r - l) // 2
        if arr[mid] == target:
            r = mid # you want to find the first one, and move r towards the middle. if you were doing 'get_last' it would be 'l = mid'
        elif arr[mid] < target:
            l = mid
        else:
            r = mid
    #post
    if arr[l] == target:
        return l
    if arr[r] == target:
        return r
    return -1


get_first([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3], 2)
