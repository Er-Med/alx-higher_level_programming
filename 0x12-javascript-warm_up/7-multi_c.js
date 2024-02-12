const nbOfOccurrences = process.argv[2];

if(isNaN(parseInt(nbOfOccurrences))){
    console.log("Missing number of occurrences");
}else{
    for(let i = 0; i < nbOfOccurrences ; i++ ){
        console.log("C is fun");
    }
}