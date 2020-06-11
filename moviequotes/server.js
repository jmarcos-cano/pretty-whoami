const movieQuotes = require('movie-quotes');


// const client = redis.createClient();
 
// client.on("error", function(error) {
//   console.error(error);
// });
 
// client.set("key", "value", redis.print);
// client.get("key", redis.print);
// console.log(movieQuotes.all());
let index = 1

movieQuotes.all.forEach( async element => {
    console.log(`${element}`);
    index++;
});