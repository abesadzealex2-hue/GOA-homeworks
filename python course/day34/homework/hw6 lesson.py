# 6) შექმენით ფუნქცია. მომხმარებელს შემოატანინე წინადადება. იპოვე და დაბეჭდე
# ყველაზე გრძელი სიტყვა ამ წინადადებაში. გამოიყენეთ while ციკლი.
# გამოიძახეთ ფუნქცია.

def function1():
    sentence = input("enter any sentence : ")
    words = sentence.split()

    biggest1 = ""
    i = 0

    while i < len(words):
        if len(words[i]) > len(biggest1):
            biggest1 = words[i]
        i += 1

    print(biggest1)

function1()
