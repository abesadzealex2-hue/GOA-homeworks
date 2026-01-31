# 1) შექმენით ფუნქცია. მომხმარებელს შემოატანინეთ ერთი მთელი რიცხვი
# n. დაბეჭდეთ თუ რამდენი ლუწი რიცხვია
# 1-დან n-მდე. გამოიძახეთ ფუნქცია.

def even1():
    number = int(input("enter any number: "))
    even = 0

    for i in range(1 , number , 1):
        if i % 2 == 0:
            even += 1

    print(even)

even1()