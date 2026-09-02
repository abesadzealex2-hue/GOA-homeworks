// 1)შექმენი ფუნქცია calculatePrice(price, quantity).

// price — პროდუქტის ფასი
// quantity — რაოდენობა
// ფუნქციამ უნდა დააბრუნოს საბოლოო ფასი.
// თუ quantity არ გადაეცა, default მნიშვნელობა იყოს 1.
// ფუნქცია გამოიძახე მინიმუმ 3 სხვადასხვა არგუმენტით.

function calculatePrice(price, quantity = 1) {
  return price * quantity;
}

console.log(calculatePrice(10, 3));
console.log(calculatePrice(50));
console.log(calculatePrice(5, 4));

function getResult(name, score = 0) {
  if (score >= 90) {
    return `${name}: Excellent`;
  } else if (score >= 70) {
    return `${name}: Good`;
  } else if (score >= 50) {
    return `${name}: Passed`;
  } else {
    return `${name}: Failed`;
  }
}

console.log(getResult("nika", 95));
console.log(getResult("anna", 80));
console.log(getResult("giorgi", 60));
console.log(getResult("lasha", 40));
console.log(getResult("Dato"));

// 3)შექმენი ფუნქცია:

// calculateShipping(price, shipping = 10)

// წესი:

// თუ პროდუქტის ფასი 100 ან მეტია → მიწოდება უფასოა.
// სხვა შემთხვევაში დაემატოს shipping.
// ფუნქციამ უნდა დააბრუნოს საბოლოო თანხა.

// გამოიძახე სხვადასხვა სიტუაციაში, მათ შორის საკუთარი shipping მნიშვნელობის გადაცემით.

function calculateShipping(price, shipping = 10){
  if(price >= 100){
    console.log('მიწოდება უფასოა')
  }else{
    console.log(price + shipping)
  }
}

calculateShipping(150)

// 4)შექმენი ფუნქცია:

// checkAge(name, age = 18)

// ფუნქციამ უნდა დააბრუნოს:

// 18 ან მეტი → "name is adult"
// 18-ზე ნაკლები → "name is minor"

// შემდეგ გამოიძახე ფუნქცია მინიმუმ 4-ჯერ.

function checkAge(name, age = 18){
  if(age >= 18){
    return 'name is adult'
  }else{
    return 'name is minor'
  }
}

checkAge('Alex')
checkAge('Rezi' , 34)
checkAge('Gega' , 14)
checkAge('Dachi' , 19)

// 5)შექმენი ფუნქცია:

// addPoints(score, points = 10)

// ფუნქციამ უნდა:

// მიიღოს არსებული ქულა.
// დაამატოს points.
// დააბრუნოს ახალი ქულა.

function addPoints(score, points = 10){
  console.log(score + points)
}

addPoints(15 , 32)

// 6)შექმენი ფუნქცია:

// createMessage(name, message = "Hello")

// ფუნქციამ უნდა დააბრუნოს:

// Hello, Goga!

// ან თუ სხვა message გადაეცა:

// Welcome, Goga!

function createMessage(name, message = "Hello"){

  if(message === 'Hello'){
    console.log('Hello, Goga!')
  }else{
    console.log('Welcome Goga')
  }
  
}

// 7)შექმენი ფუნქცია:

// calculateDiscount(price, discount = 10)

// ფუნქციამ უნდა გამოითვალოს ფასდაკლების შემდეგ დარჩენილი თანხა.


function calculateDiscount(price, discount = 10){
  console.log(price - discount )
}

calculateDiscount(90)

// 8)შექმენი ფუნქცია:

// convertTemperature(value, type = "C")

// თუ type არის "C" → Celsius გადააკეთე Fahrenheit-ში.

// ფორმულა:

// F = C * 9 / 5 + 32

// თუ type არის "F" → Fahrenheit გადააკეთე Celsius-ში.

// ფორმულა:

// C = (F - 32) * 5 / 9

function convertTemperature(value, type = "C") {
  if (type === "C") {
    return value * 9 / 5 + 32;
  } else if (type === "F") {
    return (value - 32) * 5 / 9;
  }
}

// 9)შექმენი ფუნქცია calculateSalary(salary, bonus = 0).

// ფუნქციამ უნდა:

// მიიღოს ხელფასი;
// თუ ბონუსი არ გადაეცა, ბონუსი იყოს 0;
// თუ ხელფასი 1000-ზე ნაკლებია, ბონუსი დაუმატოს ორმაგად;
// სხვა შემთხვევაში ჩვეულებრივ დაუმატოს;
// დააბრუნოს საბოლოო ხელფასი.

// მაგალითად:

// calculateSalary(800, 100)  // 1000
// calculateSalary(1500, 200) // 1700
// calculateSalary(900)       // 900

function calculateSalary(salary, bonus = 0) {
  if (salary < 1000) {
    return salary + bonus * 2;
  }
  return salary + bonus;
}

// 10)შექმენი ფუნქცია:

// checkExam(name, score = 0)

// ფუნქციამ დააბრუნოს:

// 90–100 → "name: Excellent"
// 75–89 → "name: Very Good"
// 60–74 → "name: Good"
// 50–59 → "name: Passed"
// 0–49 → "name: Failed"

// თუ ქულა არ გადაეცა, ჩაითვალოს 0. შეასრულეთ switch ით -- hint --> switch(true){...}

function checkExam(name, score = 0) {
  if (score >= 90) {
    return `${name}: Excellent`;
  } else if (score >= 75) {
    return `${name}: Very Good`;
  } else if (score >= 60) {
    return `${name}: Good`;
  } else if (score >= 50) {
    return `${name}: Passed`;
  } else {
    return `${name}: Failed`;
  }
}

checkExam('Alex')


// 11)შექმენი ფუნქცია:

// ticketPrice(age, price = 50)

// წესები:

// 5 წლამდე → უფასო
// 5–12 → ფასის 50%
// 13–59 → სრული ფასი
// 60 და ზემოთ → ფასის 30%

// მაგალითად:

// ticketPrice(4, 50)   // 0
// ticketPrice(10, 50)  // 25
// ticketPrice(25, 50)  // 50
// ticketPrice(65, 50)  // 15
// ticketPrice(20)      // 50

function ticketPrice(age, price = 50) {
  if (age < 5) {
    return 0;
  } else if (age <= 12) {
    return price * 0.5;
  } else if (age <= 59) {
    return price;
  } else {
    return price * 0.3;
  }
}

ticketPrice(25)

// 12)შექმენი ფუნქცია:

// analyzeNumber(number, limit = 100)

// ფუნქციამ უნდა დააბრუნოს:

// თუ რიცხვი უარყოფითია → "Negative"
// თუ 0-ია → "Zero"
// თუ დადებითია და limit-ზე ნაკლებია → "Small positive"
// თუ limit-ზე მეტია → "Large positive"

// შეასრულეთ ternary ით

// function analyzeNumber(number, limit = 100){
//   if(number < 0){
//     console.log('negative')
//   }else if(number === 0){
//     console.log('Zero')
//   }else if(number > 0 && number < limit){
//     console.log('Small positive')
//   }else{
//     console.log('Large positive')
//   }
// }

function analyzeNumber(number, limit = 100) {
  return number < 0 ? "Negative" : number === 0 ? "Zero" : number < limit ? "Small positive" : "Large positive";
}
