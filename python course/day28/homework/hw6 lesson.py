#6) მომხმარებელს შეაყვანინე ასაკი მანამ, სანამ არ შეიყვანს -1. დაბეჭდე რამდენი ადამიანი იყო არასრულწლოვანი, 
#სრულწლოვანი, პენსიონერი. გამოიყენე while loop + if/elif/else

count1 = 0
count2 = 0
count3 = 0
while True:
    age = int(input("enter your age : "))
    if age == -1:
        break


    if age < 18:
        count1 = count1 + 1
        

    elif age < 65 and age >= 18:
        count2 = count2 + 1
       

    else:
        count3 = count3 + 1
        
print(count1)
print(count2)
print(count3)