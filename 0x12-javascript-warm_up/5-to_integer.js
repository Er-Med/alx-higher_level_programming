let nb = process.argv[2];

if(isNaN(parseInt(nb)) ){
    console.log("Not a number");
}else{
    console.log("My number: " + parseInt(nb));
}