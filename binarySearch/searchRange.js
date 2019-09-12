const searchRange = function (nums, target) {
   let l = 0
   let r = nums.length - 1
   while (l <= r) {
      let mid = Math.floor((l + r) / 2)
      if (nums[mid] === target) {
         let l = mid
         let r = mid
         while (nums[l - 1] === target) {
            l--
         }
         while (nums[r + 1] === target) {
            r++
         }
         return [l, r]
      } else if (nums[mid] < target) {
         l = mid + 1
      } else {
         r = mid - 1
      }
   }
   return [-1, -1]
};