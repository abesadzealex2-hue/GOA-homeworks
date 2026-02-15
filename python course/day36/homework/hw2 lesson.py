# 2) შექმენი ფუქნცია რომელიც მიიღებს რაღაც ტექსტს და დაითვლის ამ ტექსტში ხმოვნების რაოდენობას

def vowel1():
    text = input("enter any text : ")
    vowel = 0
    for i in range(len(text)):
        if text[i] == "ა" or text[i] == "ე" or text[i] == "ი" or text[i] == "ო" or text[i] == "უ":
            vowel += 1
    print(vowel)

vowel1()