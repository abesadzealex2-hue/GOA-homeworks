# 7) შექმენი ფუქნცია რომელიც მომხმარებელს შემოაყვანინებს რაღაც რიცხვს და დააბრუნებს სიტყვას ეს რიცხვი დადებითია უარყოფითია თუ ნულია

def check():
    number = int(input("enter any number : "))
    if number > 0 :
        print("დადებითია")
    elif number < 0 :
        print("უარყოფითია")
    else:
        print("ნულია")
check()