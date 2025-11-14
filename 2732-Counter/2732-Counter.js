// Last updated: 11/14/2025, 8:47:53 AM
function createCounter(n){
    let count = n
    return function(){
        return count ++
    }
}
const count = createCounter(10);
console.log(count());
console.log(count());
console.log(count());
 