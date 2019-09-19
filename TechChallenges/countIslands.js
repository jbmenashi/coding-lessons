function countIslands(mat) {
   let count = 0
   let rows = mat.length
   let cols = mat[0].length
   for (let i = 0; i < rows; i++) {
      for (let j = 0; j < cols; j++) {
         if (mat[i][j] === 1) {
            checkIsland(i, j, mat)
            count++
         }
      }
   }
   return count
}

function checkIsland(row, col, mat) {
   if (!mat[row] || !mat[row][col] || mat[row][col] !== 1) {
      return
   }

   mat[row][col] = 'x'
   checkIsland(row, col + 1, mat) //right
   checkIsland(row, col - 1, mat) //left
   checkIsland(row + 1, col, mat) //top
   checkIsland(row - 1, col, mat) //bottom
}


countIslands([
   ["1", "1", "1", "1", "0"],
   ["1", "1", "0", "1", "0"],
   ["1", "1", "0", "0", "0"],
   ["0", "0", "0", "0", "0"]
])