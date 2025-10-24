#5) მომხმარებელს შემოატანინე:
#--> მომხმარებლის სახელი (username)
#--> პაროლი (password)
#შეამოწმე:
#თუ მომხმარებელი არის "admin" და პაროლი არის 'superSecretPassword' → "მოგესალმები, ადმინ!"
#თუ მომხმარებელი "guest" და პაროლი არის "1234" → "მოგესალმები, სტუმარო!"
#სხვა შემთხვევაში → "მომხმარებელი არ მოიძებნა!"


username = ("enter your username:")
password = int(input("enter your password:"))

if username == "admin" and password == "supersecretpassword":
    print ("მოგესალმებით ადმინ")

elif username == "guest" and password == 1234:
    print ("მოგესალმები,სტუმარო")

else:
    print ("მომხმარებელი არ მოიძებნა")