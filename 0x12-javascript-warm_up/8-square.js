const nbOfOccurrences = process.argv[2];
let char = "X"
if(isNaN(parseInt(nbOfOccurrences))){
    console.log("Missing size");
}else{
    for (let i = 0; i<nbOfOccurrences; i++) {
        console.log(char.repeat(nbOfOccurrences));
    }
}