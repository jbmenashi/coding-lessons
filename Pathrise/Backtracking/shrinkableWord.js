const isShrinkable = (word, lexicon) => {
   if (word.length === 1) {
      return true
   }
   else {
      for (let i = 0; i < word.length; i++) {
         let shrunkenWord = word.slice(0, i) + word.slice(i + 1)
         if (lexicon.includes(shrunkenWord) && isShrinkable(shrunkenWord, lexicon)) {
            return true
         }
      }
      return false
   }
}

const lex = ['startling', 'starling', 'staring', 'string', 'sting', 'sing', 'sin', 'in', 'i']

isShrinkable('startling', lex)