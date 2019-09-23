var countCharacters = function (words, chars) {
   let count = 0
   let hash = {}
   for (let char of chars) {
      hash[char] ? hash[char]++ : hash[char] = 1
   }
   for (let word of words) {
      let clone = Object.assign({}, hash)
      for (let char of word) {
         clone[char] && clone[char] > 0 ? clone[char]-- : word = ''
      }
      count = count + word.length
   }

   return count
};