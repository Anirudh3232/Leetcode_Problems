// Last updated: 11/14/2025, 8:47:51 AM
function createHelloWorld(){
    return function(){
        return "Hello World"
    }
}

const f = createHelloWorld();
console.log(f());