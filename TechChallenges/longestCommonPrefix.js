var longestCommonPrefix = function (strs) {
   if (!strs) {
      return ''
   }
   let prefix = strs[0]
   let l = 0
   let r = strs[0].length - 1
   for (let i = 1; i < strs.length; i++) {
      let mid = Math.floor((l + r) / 2)
      if (strs[0][mid] === strs[i][mid]) {
         for (let j = mid; j >= 0; j--) {
            if (strs[0][j] !== strs[i][j]) {
               return ''
            } else {
               prefix = strs[0].slice(0, mid)
            }
         }
      } else if (strs[0][mid] !== strs[i][mid]) {
         mid = mid - 1
      }

   }
   if (prefix === strs[0] && !strs[1].includes(strs[0])) {
      return ''
   }
   return prefix

};