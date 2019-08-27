function firstUniqChar(s) {
   // Write your code here
   let hash = {}
   for (let i = 0; i < s.length; i++) {
      if (hash[s[i]]) {
         hash[s[i]]++
      } else {
         hash[s[i]] = 1
      }
   }
   for (let i = 0; i < s.length; i++) {
      if (hash[s[i]] === 1) {
         return i
      }
   }
}