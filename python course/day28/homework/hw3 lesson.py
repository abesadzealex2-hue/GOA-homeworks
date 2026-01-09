#3) მომხმარებელს შეაყვანინე პაროლი. თუ პაროლი მეტია ან ტოლია 8 სიმბოლოზე →
#"პაროლი საკმარისად ძლიერია", თუ ნაკლებია → "პაროლი სუსტია", გამოიყენე while,თუ მომხმარებელი
#სუსტ პაროლს შემოიყვანს რომ მომხმარებელმა ისევ შეიყვანოს ძლიერი პაროლი.

password = input("enter any password : ")

size = len(password)

if size >= 8:
    print("პაროლი საკმარისად ძლიერია")

elif size < 8:
    print("პაროლი სუსტია")

    while True:
        password = input("enter any password : ")
        size = len(password)
        if size >= 8:
            print("პაროლი საკმარისად ძლიერია")
            break

        elif size < 8:
            print("პაროლი სუსტია")
