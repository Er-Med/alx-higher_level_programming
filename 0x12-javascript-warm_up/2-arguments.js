// Check the number of arguments passed to the script
const numOfArgs = process.argv.length - 2; // Subtract 2 to exclude 'node' and the script filename

// Check the number of arguments and print the appropriate message
if (numOfArgs === 0) {
    console.log("No argument");
} else if (numOfArgs === 1) {
    console.log("Argument found");
} else {
    console.log("Arguments found");
}