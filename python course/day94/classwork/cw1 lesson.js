// 1)შექმენი function expression სახელად checkNumber, რომელსაც გადაეცემა რიცხვი.

// ფუნქციამ უნდა დააბრუნოს:

// "Positive Even" — დადებითი და ლუწი
// "Positive Odd" — დადებითი და კენტი
// "Negative Even" — უარყოფითი და ლუწი
// "Negative Odd" — უარყოფითი და კენტი
// "Zero" — თუ რიცხვი 0-ია , use ternary

// let checkNumber = function(num) {
//     return num === 0 ? "Zero" : (num > 0 ? "Positive " : "Negative ") + (num % 2 === 0 ? "Even" : "Odd");
// };

// console.log(checkNumber(-4))

// 2)შექმენით arrow ფუნქცია რომელსაც გადაეცემა ერთ პარამეტრი name ფუნქციამ უნდა შეამოწმოს
//  if else ით იწყება თუ არა ეს სახელი "გ" ასოზე , თუ იწყება დააბრუნე good
//  name სხვა შემთხვევაში დააბრუნე "still good name"

// let checkName = (name) => {
//   if (name.startsWith("გ")) {
//     return "good name";
//   } else {
//     return "still good name";
//   }
// };

// 3)შექმენით arrow ფუნქცია რომელსაც გადაეცემა ერთ პარამეტრი num , შენი დავალებაა შეამოწმო ეს რიცხვი ლუწია
// თუ კენტია , use ternary and single line block stytax

let checkEvenOdd = num => num % 2 === 0 ? "luwia" : "kentia";

console.log(checkEvenOdd(4));
console.log(checkEvenOdd(7));