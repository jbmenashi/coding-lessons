# given a list of N queens, determine if you can put them on an NxN
# chess board in such a way that they aren't attacking each other

# Brute Force would be just place every queen in every combo, very bad
# It's n**n runtime complexity

# base case, if we don't have any more to place we're good

def find_first_valid_board(board, row, col, queens_remaining):
   if queens_remaining == 0;
      printBoard(board)
      return True
   else:
      total_rows = len(board)
      total_cols = len(board[0])
      for r in range(row, total_rows):
         for c in range(col, total_cols):
            board[r][c] = 'Q'
            queens_remaining -= 1
            # need a helper function, "if I have time later, I'll write it"
            if not_under_attack(r, c) && find_first_valid_board(board, row, col, queens_remaining):
               return True
            board[r][c] = ''
            queens_remaining += 1
   return False
