#8) მომხმარებელს შეაყვანინე 5 რიცხვი while loopით, დაითვალე მათი საშუალო, თუ საშუალო > 50 დაბეჭდე 
#"დიდი საშუალო" წინააღმდეგ შემთხვევაში "პატარა საშუალო"

i = 0
sum = 0
while i < 5 :
    number = int(input("enter any number : "))
    sum = sum + number

    i = i + 1

if sum / 5 > 50:
    print("დიდი საშუალო")

else:
    print("პატარა საშუალო")

print(sum / 5)