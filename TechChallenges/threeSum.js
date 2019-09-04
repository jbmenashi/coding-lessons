const threeSum = (arr) => {
    let sorted = arr.sort((a, b) => a - b)
    // console.log(sorted)
    for (let i = 0; i < sorted.length; i++) { // -3
        for (let j = i; j < sorted.length ; j++) { // 3
            let sum = sorted[i] + sorted[j] // 0
            // console.log(sum)
            let target = 0 - sum // target = 0
            let foundEl = binarySearch(sorted, target)
            // console.log('foundEl', foundEl)
            if (foundEl || foundEl === 0) {
                return [sorted[i], sorted[j], foundEl]
            }
        }
    }
    return 'None'
}

const binarySearch = (arr, target) => { // [-3, 3, 2, 0], 0 
    let low = 0 // 0 
    let high = arr.length - 1 // 3
    while (low < high) {
        let mid = Math.floor((low + high) / 2) // 1
        if (target === arr[mid]) { 
            return arr[mid]
        }
        else if (target < arr[mid]) {
            low = mid + 1
        }
        else {
            high = mid - 1
        }
    }
}


console.log(threeSum([7, -10, 4, 5, 3, -12]))
console.log(threeSum([-3, 3, 2, 0]))
console.log(threeSum([1, 2, 3, 4]))