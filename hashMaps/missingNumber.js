const missingNumber = (nums) => {
   numSet = new Set(nums)
   for (let i = 0; i <= nums.length; i++) {
      if (!numSet.has(i)) {
         return i
      }
   }
}