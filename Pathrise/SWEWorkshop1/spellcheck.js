// the problem you did for the interview,
// given a list of words, check to see if the
// test word is in there, with the * wildcards

//write a function that checks ONE word

const checkEquality = (word, query) => {
   if (word.length != query.length) {
      return false
   }
   for (let i = 0; i < word.length; i++) {
      if (query[i] !== '*' && query[i] !== word[i]) {
         return false
      }
   }
   return true
}

// then call that function for the whole array

const isMember = (words, query) => {
   for (let el of words) {
      if (checkEquality(el, query)) {
         return true
      }
   }
   return false
}

words = ['foo', 'bar', 'baz']
console.log(isMember(words, 'foo'))
console.log(isMember(words, 'b*z'))
console.log(isMember(words, 'blob'))
console.log(isMember(words, 'fot'))
