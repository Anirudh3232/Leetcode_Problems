// Last updated: 11/14/2025, 8:47:52 AM
function createCounter(init){
    let currentvalue = init;
    return{
        increment: function(){
            return ++currentvalue
        },
        decrement: function(){
            return --currentvalue
        },
        reset: function(){
            currentvalue = init;
            return currentvalue;
        }
    };

}


  const counter = createCounter(5)
  counter.increment(); // 6
  counter.reset(); // 5
  counter.decrement(); // 4
 