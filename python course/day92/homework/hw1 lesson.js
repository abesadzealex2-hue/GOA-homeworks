console.log(1)
let score = 87;
let result1 = score >= 90 ? "Excellent" : score >= 75 ? "Very Good" : score >= 60 ? "Good" : score >= 40 ? "Passed" : "Failed";

console.log(result1);


console.log(2)
let age = 20;
let isStudent = true;
let result2 = age < 18 ? "Minor" : isStudent ? "Adult student" : age >= 60 ? "Senior" :"Adult";

console.log(result2);

console.log(3)
let number1 = -14;
let number2 = number1 > 0 ? "დადებითი" : number1 < 0 ? "ნეგატიური" : "ნოლი";
let number3 = number1 === 0 ? "Zero" : number1 % 2 === 0 ? "Even" : "Odd";

console.log(4)

let username = "adminGoga";

if(username === ""){
    console.log("Username is empty")
} else if(username.startsWith("admin")){
    console.log("Admin")
} else {
    console.log("Unknown user")
}

console.log(5)
let temperature = 28;

let temperature2 = temperature < 0 ? "Freezing" : temperature <= 10 ? "Cold" : temperature <= 20 ? "Cool" : temperature <= 30 ? "Warm" : "Hot";

console.log(temperature2);

console.log(6)
let a = 45;
let b = 78;
let c = 32;

let max = a >= b && a >= c ? a : b >= c ? b : c;

console.log(max);

console.log(7)

let day = 4;

switch (day) {
  case 1:
    console.log("Monday");
    break;
  case 2:
    console.log("Tuesday");
    break;
  case 3:
    console.log("Wednesday");
    break;
  case 4:
    console.log("Thursday");
    break;
  case 5:
    console.log("Friday");
    break;
  case 6:
    console.log("Saturday");
    break;
  case 7:
    console.log("Sunday");
    break;
  default:
    console.log("Invalid day");
}

console.log(8)
let grade = "B";

switch (grade) {
  case "A":
    console.log("Excellent");
    break;
  case "B":
    console.log("Very Good");
    break;
  case "C":
    console.log("Good");
    break;
  case "D":
    console.log("Passed");
    break;
  case "F":
    console.log("Failed");
    break;
  default:
    console.log("Invalid grade");
}

console.log(9)