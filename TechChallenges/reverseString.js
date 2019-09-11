let reverseString = function (s) {
   let arr = s.split(''),
      left = 0,
      right = arr.length - 1;
   while (left < right) {
      let temp = arr[left];
      arr[left] = arr[right];
      arr[right] = temp;
      ++left;
      --right;
   }
   return arr.join('');
};