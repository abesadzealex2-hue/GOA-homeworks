// 7)მოცემულია კოდი:
// let name = "Goga";
// function first() {
//     let age = 20;
//     // let city = "Tbilisi";
// }
// function second() {
//     let city = "Tbilisi";
//     console.log(name);
//     console.log(age);
//     console.log(city);
//     }

// second();
// }
// first();
// დავალება:
// მიუთითე თითოეული ცვლადის Scope.
// რომელი ცვლადის გამოყენება შეუძლია second() ფუნქციას?
// რომელი ცვლადის გამოყენება არ შეუძლია first() ფუნქციას? --- ვერ მიწვდა city ს
// შეცვალე კოდი ისე, რომ city დაბეჭდო first() ფუნქციიდანაც. --- გადავაკეთე

// second ფუნქციას შეუძლია მიწვდეს name , age , city ანუ ყველას


// 8)იპოვე შეცდომა Scope-ში
// let score = 100;

// if (score > 50) {
//     let message = "Passed";
// }

// console.log(message);

// დავალება:
// ახსენი, რატომ იძლევა ეს კოდი შეცდომას და შეცვალე ისე, რომ "Passed" დაიბეჭდოს.
// console არ აქვს წვდომა ლოკალურ scope ზე და მისთვის ეს ცვლადი არ არსებობს.


// 9)let x = 10;

// function outer() {
//     let x = 20;

//     function middle() {
//         let y = 30;

//         function inner() {
//             let x = 40;

//             console.log(x);
//             console.log(y);
//         }

//         inner();
//     }

//     middle();
// }

// outer();

// დავალება:

// რა დაიბეჭდება?
// inner()-ში რომელი x გამოიყენება? --- 40 და 30
// თუ inner()-დან let x = 40 წავშლით, რომელი x იქნება გამოყენებული? --- 20
// თუ middle()-დანაც წავშლით let y = 30-ს, რა მოხდება console.log(y)-ზე? --- Error იგრეკი არ გვაქვს სხვაგან.

// 10)let country = "Georgia";

// function school() {
//     let students = 20;

//     if (students > 10) {
//         let teacher = "Goga";

//         console.log(country); --- georgia
//         console.log(students); --- 20
//         console.log(teacher); --- goga
//     }
// }

// დავალება: თითოეულ console.log()-თან მიუწერე:

// country → ______ scope || global
// students → ______ scope || local
// teacher → ______ scope  || local .