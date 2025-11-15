#მომხმარებელს შემოატანინე რიცხვი, მანამ სანამ არ შემოიტანს  ტექტს - 'გამოთვალე საშუალო'. როგორც კი ამ ტექტს შემოიყვანს
# დაპრინტეთ ყველა შემოტანილი რიცხვის საერთო საშუალო არითმეტიკული.

sum_number=0
len_number=0

number=input("enter any number:")

while number != "გამოთვალე საშუალო":
    len_number=len_number + 1
    sum_number=sum_number+int(number)
    number=input("enter any number:")

print (sum_number/len_number)