// let checkNumber = num => num > 0 ? "Positive" : num < 0 ? "Negative" : "Zero";
//1

//2

// let getGrade = function(score) {
//     if (score === undefined || score < 0 || score > 100) return "Invalid score";
//     if (score >= 90) return "A";
//     if (score >= 80) return "B";
//     if (score >= 70) return "C";
//     if (score >= 60) return "D";
//     return "F";
// };

// getGrade(45)


//4
// let checkWord = (word) => {
//   let lowerWord = word.toLowerCase();
//   if (lowerWord.startsWith("a")) {
//     return "Starts with A";
//   } else {
//     return "Does not start with A";
//   }
// };

//5

// let analyzeNumbers = function(a, b, c) {
//   return Math.max(a, b, c);
// };




//6


// let analyzeText = (text) => {
//   console.log(text.length);
//   console.log(text.toUpperCase());
//   console.log(text.startsWith("Hello"));
// }


//7



// let calculatePrice = (price, discount) => {
//   if (discount >= 50) return "Discount too high";
//   if (discount < 0) return "Invalid discount";
//   return price - (price * discount / 100);
// };



//8
// let validatePassword = (password) => {
//   let isLongEnough = password.length >= 8;
//   let includesAt = password.includes("@");
//   let startsWithUpper = password[0] >= "A" && password[0] <= "Z";
//9




// let validateUser = (username , age , password) =>{
//     if(username != "" && age >= 18 && password.length >= 8){
//         return "User is valid"
//     }else{
//         return "User is invalid"
//     }
//}