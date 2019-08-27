# given a diction, reduce a word letter by letter and have it be in the dictionary
# can remove a letter from wherever

# so the base case is get when its not a valid word

def is_shrinkable(word, lexicon):
   if len(word) == 1:
      return True
   else:
      for letter_index in range(len(word)):
         shrunken_word = word[:letter_index] + word[letter_index + 1:]
         if shrunken_word in lexicon and is_shrinkable(shrunken_word, lexicon):
            return True
   return False