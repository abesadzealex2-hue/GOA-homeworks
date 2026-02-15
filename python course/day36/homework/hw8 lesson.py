# 8) შექმენი ფუქნცია რომელიც მიიღებს რაღაც ტექსტს და ასევე რაღაც რიცხვს, ტექსტსში ყველა ასოა აქციე დიდად და რიცხვითი
# მნიშვნელობა გადააქცია სტრინგის ტიპად.

def fun1():
    text = input("enter any text : ")
    number = int(input("enter any number : "))
    
    text = text.upper()
    number = str(number)
    
    print(text)
    print(number)
fun1()