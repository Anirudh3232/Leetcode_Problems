// Last updated: 11/14/2025, 8:47:52 AM
var map = function(arr, fn) {
    let result = [];
    for (let i = 0; i < arr.length; i++) {
        result.push(fn(arr[i], i));
    }
    return result;
};

// Example usage:
const arr = [1, 2, 3, 4];
const fn = (value, index) => value * index;

console.log(map(arr, fn)); // Expected Output: [0, 2, 6, 12]
