#5) შექმენი ნებისმიერი list 5 ელემენტით, მომხმარებელს ჰკითხე: გინდა list-ის გასუფთავება?
#(yes/no), თუ პასუხი "yes"  გამოიყენე clear(), ბოლოს დაბეჭდე list

list = ["Nika" , "Goga" , 44 , 12.5 , False , True]
answer = input("do u wont to clear the list??? answer - yes or no : ")
if answer == "yes":
    list.clear()
    print(list)
elif answer == "no":
    print("list did not changed")
    print(list)
else:
    print("i dont know what do u want")