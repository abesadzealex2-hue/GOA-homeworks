# 3) შექმენით ფუნქცია. შექმენით რიცხვებით სავსე სია, დაბეჭდეთ
# ამ სიის ყველა ლუწი ელემენტის ჯამი.
# გამოიყენე for ციკლი.  გამოიძახეთ ფუნქცია.

def function1():
    numbers = [1 , 6 ,9 , 5 ,60 , 191 , 21 ,555 ,12]
    even = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            even = even + numbers[i]
    print(even)
function1()